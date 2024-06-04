from typing import Any

from budget.api_output import DjangoApiOutput
from rest_framework import status
from rest_framework.response import Response


class ExecuteUseCaseOnGetMixin:
    """Mixin para executar casos de uso ao lidar com solicitações GET."""

    use_case: Any | None = None
    use_case_retrieve: Any | None = None
    use_case_output: Any | None = None
    use_case_output_retrieve: Any | None = None
    image_fields: Any | None = None
    query_serializer: Any | None = None

    def get(self, request, *args, **kwargs):
        """
        Manipula solicitações GET.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.

        Returns:
        -------
            Resposta HTTP.
        """
        try:
            uc = self.execute_use_case_retrieve(request, *args, **kwargs)
            response = uc.get_response() if hasattr(uc, "get_response") else Response(uc.data, status=status.HTTP_200_OK)
            if self.image_fields:
                response = self.apply_domain_host_in_image_fields(request, response, *args, **kwargs)
            if response.data is None:
                return Response(
                    {"detail": "object not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return response
        except self.Http400Error as e:
            print(e)
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            if hasattr(e, "code") and e.code < 500:
                return Response(
                    {"detail": e.args[0], "exception_name": e.__class__.__name__},
                    status=e.code,
                )
            raise

    def execute_use_case_retrieve(self, request, *args, **kwargs):
        """
        Executa o caso de uso do método retrieve.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.

        Returns:
        -------
            Instância do caso de uso.
        """
        use_case_class = self.get_use_case_retrieve()
        output_response = self.get_use_case_output_retrieve()
        if output_response:
            use_case_class.output_response = output_response
        uc = use_case_class(**self.get_use_case_kwargs_retrieve(request, *args, **kwargs))
        return uc.execute()

    def get_use_case_retrieve(self):
        """
        Obtém a classe de caso de uso do método retrieve.

        Returns:
        -------
            Classe de caso de uso.
        """
        return self.use_case_retrieve if self.use_case_retrieve else self.use_case

    def get_use_case_kwargs_retrieve(self, request, *args, **kwargs):
        """
        Obtém os argumentos do caso de uso do método retrieve.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.

        Returns:
        -------
            Argumentos do caso de uso.
        """
        data = self.get_use_case_kwargs(request, *args, **kwargs)
        if self.query_serializer:
            serializer = self.query_serializer(data=data)
            if not serializer.is_valid():
                raise self.Http400Error(serializer.errors)
            data = {**data, **serializer.validated_data}
        return data

    def get_use_case_kwargs(self, request, *args, **kwargs):
        """
        Obtém os argumentos do caso de uso.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.

        Returns:
        -------
            Argumentos do caso de uso.
        """
        return {}

    def get_use_case_output_retrieve(self):
        """
        Obtém a saída do caso de uso do método retrieve.

        Returns:
        -------
            Saída do caso de uso.
        """
        return self.use_case_output_retrieve if self.use_case_output_retrieve else self.use_case_output

    def apply_domain_host_in_image_fields(self, request, response, *args, **kwargs):
        """
        Aplica o domínio e o host nos campos de imagem na resposta.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            response: Resposta HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.

        Returns:
        -------
            Resposta HTTP com domínio e host aplicados nos campos de imagem.
        """

        def nested_update(output_response):
            if isinstance(output_response, dict):
                for key, value in output_response.items():
                    if isinstance(value, dict | list):
                        nested_update(value)
                    elif key in self.image_fields:
                        output_response[key] = f"{request.scheme}://{request.get_host()}{value}" if value else None
            elif isinstance(output_response, list):
                for item in output_response:
                    nested_update(item)

        nested_update(response.data)
        return response

    class Http400Error(Exception):
        """Exceção para erros de solicitação HTTP 400."""

        def __init__(self, message):
            super().__init__(message)
            self.message = message


class ExecuteUseCaseOnDestroyMixin:
    """Mixin para executar casos de uso ao lidar com solicitações DELETE."""

    use_case: Any | None = None
    use_case_destroy: Any | None = None
    use_case_output: type[DjangoApiOutput] | None = None
    use_case_output_destroy: Any | None = None
    image_fields: Any | None = None

    def delete(self, request, *args, **kwargs):
        """
        Manipula solicitações DELETE.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        try:
            uc = self.execute_use_case_destroy(request, *args, **kwargs)
            response = uc.get_response()
            if response.data is None:
                return Response(
                    {"detail": "object not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return response
        except self.Http400Error as e:
            print(e)
            return Response(e.args[0], status=e.code)
        except Exception as e:
            if hasattr(e, "code") and e.code < 500:
                return Response({"detail": e.args[0]}, status=e.code)
            raise

    def execute_use_case_destroy(self, request, *args, **kwargs):
        """
        Executa o caso de uso do método destroy.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        use_case_class = self.get_use_case_destroy()
        use_case_class.output_response = self.get_use_case_output_destroy()
        uc = use_case_class(**self.get_use_case_kwargs_destroy(request, *args, **kwargs))
        return uc.execute()

    def get_use_case_destroy(self):
        """
        Obtém a classe de caso de uso do método destroy.

        Returns:
        -------
            Classe de caso de uso.
        """
        return self.use_case_destroy if self.use_case_destroy else self.use_case

    def get_use_case_kwargs_destroy(self, request, *args, **kwargs):
        """
        Obtém os argumentos do caso de uso do método destroy.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        return self.get_use_case_kwargs(request, *args, **kwargs)

    def get_use_case_kwargs(self, request, *args, **kwargs):
        """
        Obtém os argumentos do caso de uso.

        Args:
        ----
        request: Objeto de solicitação HTTP.
        """
        return {}

    def get_use_case_output_destroy(self):
        """Obtém a saída do caso de uso do método destroy."""
        return self.use_case_output_destroy if self.use_case_output_destroy else self.use_case_output

    class Http400Error(Exception):
        """Exceção para erros de solicitação HTTP 400."""

        pass


class ExecuteUseCaseOnUpdateMixin:
    """Mixin para executar casos de uso ao lidar com solicitações PUT e PATCH."""

    use_case = None
    use_case_update = None
    use_case_output = None
    use_case_output_update = None
    serializer = None
    image_fields = None

    def put(self, request, *args, **kwargs):
        """
        Manipula solicitações PUT.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        serializer = self.get_serializer(request)
        return self.update_data(request, serializer, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Manipula solicitações PATCH.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        serializer = self.get_serializer(request, partial=True)
        return self.update_data(request, serializer, *args, **kwargs)

    def update_data(self, request, serializer, *args, **kwargs):
        """
        Executa a atualização de dados.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            serializer: Serializador.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        try:
            if serializer.is_valid():
                uc = self.execute_use_case_update(request, serializer.validated_data, *args, **kwargs)
                response = uc.get_response()
                if self.image_fields:
                    response = self.apply_domain_host_in_image_fields(request, response, *args, **kwargs)
                if response.data is None:
                    return Response(
                        {"detail": "object not found"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                return response
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            if hasattr(e, "code") and isinstance(type(e.code), int) and e.code < 500:
                return Response(
                    {"detail": e.args[0], "exception_name": e.__class__.__name__},
                    status=e.code,
                )
            raise

    def get_serializer(self, request, partial=False):
        """
        Obtém a serializer.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            partial: Indica se a atualização é parcial.
        """
        serializer = self.serializer(
            data=request.data,
            context={
                "request": request,
            },
            partial=partial,
        )
        return serializer

    def execute_use_case_update(self, request, data, *args, **kwargs):
        """
        Executa o caso de uso do método update.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            data: Dados.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        use_case_class = self.get_use_case_update()
        use_case_class.output_response = self.get_use_case_output_update()
        uc = use_case_class(**self.get_use_case_kwargs_update(request, data, *args, **kwargs))
        return uc.execute()

    def get_use_case_update(self):
        """Obtém a classe de caso de uso do método update."""
        return self.use_case_update if self.use_case_update else self.use_case

    def get_use_case_kwargs_update(self, request, data, *args, **kwargs):
        """Obtém os argumentos do caso de uso do método update."""
        return self.get_use_case_kwargs(request, data, *args, **kwargs)

    def get_use_case_kwargs(self, request, data, *args, **kwargs):
        """Obtém os argumentos do caso de uso."""
        return {}

    def get_use_case_output_update(self):
        """Obtém a saída do caso de uso do método update."""
        return self.use_case_output_update if self.use_case_output_update else self.use_case_output

    def apply_domain_host_in_image_fields(self, request, response, *args, **kwargs):
        """
        Aplique o domínio e o host nos campos de imagem na resposta.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            response: Resposta HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """

        def nested_update(output_response):
            """Atualiza campos de imagem na resposta."""
            if isinstance(output_response, dict):
                for key, value in output_response.items():
                    if isinstance(value, dict | list):
                        nested_update(value)
                    elif key in self.image_fields:
                        output_response[key] = f"{request.scheme}://{request.get_host()}{value}" if value else None
            elif isinstance(output_response, list):
                for item in output_response:
                    nested_update(item)

        nested_update(response.data)
        return response

    class Http400Error(Exception):
        """Exceção para erros de solicitação HTTP 400."""

        pass


class ExecuteUseCaseOnPutMixin:
    """Mixin para executar casos de uso ao lidar com solicitações PUT."""

    use_case: Any | None = None
    use_case_output: Any | None = None
    image_fields: Any | None = None

    def put(self, request, *args, **kwargs):
        """
        Manipula solicitações PUT.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        self.use_case.output_response = self.use_case_output
        try:
            uc = self.execute(request, *args, **kwargs)
            response = uc.get_response()
            if response.data is None:
                return Response(
                    {"detail": "object not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            return response
        except self.Http400Error as e:
            print(e)
            return Response(e.args[0], status=e.code)
        except Exception as e:
            if hasattr(e, "code") and e.code < 500:
                return Response({"detail": e.args[0]}, status=e.code)
            raise

    def execute(self, request, *args, **kwargs):
        """Executa o caso de uso."""
        uc = self.use_case(**self.get_use_case_kwargs(request, *args, **kwargs))
        return uc.execute()

    def get_use_case_kwargs(self, request, *args, **kwargs):
        """Obtém os argumentos do caso de uso."""
        return {}

    class Http400Error(Exception):
        """Exceção para erros de solicitação HTTP 400."""

        pass


class ExecuteUseCaseOnCreateMixin:
    """Mixin para executar casos de uso ao lidar com solicitações POST."""

    use_case: Any | None = None
    use_case_create: Any | None = None
    use_case_output: type[DjangoApiOutput] | None = None
    use_case_output_create = None
    image_fields: Any | None = None
    serializer: Any | None = None
    serializer_create: Any | None = None
    serializer_instance: Any | None = None

    def post(self, request, *args, **kwargs):
        """
        Manipula solicitações POST.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        self.serializer_instance = self.get_serializer_create()(data=request.data, context={"request": request})
        if self.serializer_instance.is_valid():
            try:
                uc = self.execute_use_case_create(request, *args, data=self.serializer_instance.data, **kwargs)
                response = uc.get_response() if hasattr(uc, "get_response") else Response(uc.data, status=status.HTTP_200_OK)
                if response.data is None:
                    return Response(
                        {"detail": "object not found"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                return response
            except self.Http400Error as e:
                print(e)
                return Response(e.args[0], status=e.code)
            except Exception as e:
                response = self.catch_error(e)

                if isinstance(response, Response):
                    return response
                raise

        return Response(self.serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def execute_use_case_create(self, request, data, *args, **kwargs):
        """
        Executa o caso de uso do método create.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            data: Dados.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        use_case_class = self.get_use_case_create()
        use_case_class.output_response = self.get_use_case_output_create()
        uc = use_case_class(data=data, **self.get_use_case_kwargs_create(request, *args, **kwargs))
        return uc.execute()

    def get_use_case_create(self):
        """Obtém a classe de caso de uso do método create."""
        return self.use_case_create if self.use_case_create else self.use_case

    def get_use_case_kwargs_create(self, request, *args, **kwargs):
        """
        Obtém os argumentos do caso de uso do método create.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        return self.get_use_case_kwargs(request, *args, **kwargs)

    def get_use_case_kwargs(self, request, *args, **kwargs):
        """
        Obtém os argumentos do caso de uso.

        Args:
        ----
            request: Objeto de solicitação HTTP.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos de palavra-chave adicionais.
        """
        return {}

    def get_use_case_output_create(self):
        """Obtém a saída do caso de uso do método create."""
        return self.use_case_output_create if self.use_case_output_create else self.use_case_output

    def get_serializer_create(self):
        """Obtém a serializer de criação."""
        return self.serializer_create if self.serializer_create else self.serializer

    def catch_error(self, error: Exception):
        """
        Obtém a resposta de erro.

        Args:
        ----
            error: Exceção.
        """
        if hasattr(error, "code") and error.code < 500:
            return Response({"detail": error.args[0]}, status=error.code)
        raise

    class Http400Error(Exception):
        """Exceção para erros de solicitação HTTP 400."""

        pass
