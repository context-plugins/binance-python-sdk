from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.buy_a_binance_code_trade_error import BuyABinanceCodeTradeErrorBody, buy_a_binance_code_trade_error_mapper
from ..errors.create_a_binance_code_user_data_error import (
    CreateABinanceCodeUserDataErrorBody,
    create_a_binance_code_user_data_error_mapper,
)
from ..errors.fetch_rsa_public_key_user_data_error import (
    FetchRsaPublicKeyUserDataErrorBody,
    fetch_rsa_public_key_user_data_error_mapper,
)
from ..errors.fetch_token_limit_user_data_error import (
    FetchTokenLimitUserDataErrorBody,
    fetch_token_limit_user_data_error_mapper,
)
from ..errors.redeem_a_binance_code_user_data_error import (
    RedeemABinanceCodeUserDataErrorBody,
    redeem_a_binance_code_user_data_error_mapper,
)
from ..errors.verify_a_binance_code_user_data_error import (
    VerifyABinanceCodeUserDataErrorBody,
    verify_a_binance_code_user_data_error_mapper,
)
from ..models.sapi_v1_giftcard_buy_code_response import SapiV1GiftcardBuyCodeResponse
from ..models.sapi_v1_giftcard_buy_code_token_limit_response import SapiV1GiftcardBuyCodeTokenLimitResponse
from ..models.sapi_v1_giftcard_create_code_response import SapiV1GiftcardCreateCodeResponse
from ..models.sapi_v1_giftcard_cryptography_rsa_public_key_response import (
    SapiV1GiftcardCryptographyRsaPublicKeyResponse,
)
from ..models.sapi_v1_giftcard_redeem_code_response import SapiV1GiftcardRedeemCodeResponse
from ..models.sapi_v1_giftcard_verify_response import SapiV1GiftcardVerifyResponse
from ..server.server import Server


class GiftCard:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GiftCardWithRawResponse(client, server, auth)

    def buy_a_binance_code_trade(
        self,
        base_token: str,
        face_token: str,
        base_token_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardBuyCodeResponse:
        """This API is for buying a fixed-value Binance Code, which means your Binance Code will be redeemable to a
        token that is different to the token that you are paying in. If the token you’re paying and the redeemable token
        are the same, please use the Create Binance Code endpoint. You can use supported crypto currency or fiat token
        as baseToken to buy Binance Code that is redeemable to your chosen faceToken. Once successfully purchased, the
        amount of baseToken would be deducted from your funding wallet.

        To get started with, please make sure:
        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            face_token: The token you want to buy, example BNB. If faceToken = baseToken, it's the same as createCode
                endpoint.
            base_token_amount: The base token asset quantity, example 1.002
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code creation

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.buy_a_binance_code_trade(
            base_token,
            face_token,
            base_token_amount,
            timestamp,
            signature,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def create_a_binance_code_user_data(
        self,
        token: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardCreateCodeResponse:
        """This API is for creating a Binance Code. To get started with, please make sure:

        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            token: The coin type contained in the Binance Code
            amount: The amount of the coin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code creation

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.create_a_binance_code_user_data(
            token, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def fetch_rsa_public_key_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardCryptographyRsaPublicKeyResponse:
        """This API is for fetching the RSA Public Key. This RSA Public key will be used to encrypt the card code.
        Please note that the RSA Public key fetched is valid only for the current day.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            RSA Public Key.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fetch_rsa_public_key_user_data(
            timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def fetch_token_limit_user_data(
        self,
        base_token: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardBuyCodeTokenLimitResponse:
        """This API is to help you verify which tokens are available for you to purchase fixed-value gift cards as
        mentioned in section 2 and it's limitation.

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token limit

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.fetch_token_limit_user_data(
            base_token, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    def redeem_a_binance_code_user_data(
        self,
        code: str,
        timestamp: int,
        signature: str,
        *,
        external_uid: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardRedeemCodeResponse:
        """This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding
        wallet.

        Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any
        Binance Code that day.

        Weight(IP): 1

        Args:
            code: Binance Code
            timestamp: UTC timestamp in ms
            signature: Signature
            external_uid: Each external unique ID represents a unique user on the partner platform. The function helps
                you to identify the redemption behavior of different users, such as redemption frequency and amount. It
                also helps risk and limit control of a single account, such as daily limit on redemption volume,
                frequency, and incorrect number of entries. This will also prevent a single user account reach the
                partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the
                User ID of your users if you have different users redeeming Binance codes on your platform. To protect
                user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters).
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redeemed Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.redeem_a_binance_code_user_data(
            code,
            timestamp,
            signature,
            external_uid=external_uid,
            recv_window=recv_window,
            request_options=request_options,
        ).unwrap()

    def verify_a_binance_code_user_data(
        self,
        reference_no: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardVerifyResponse:
        """This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference
        number.

        Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to
        verify any binance code for that hour.

        Weight(IP): 1

        Args:
            reference_no: reference number
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code Verification

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return self._with_raw_response.verify_a_binance_code_user_data(
            reference_no, timestamp, signature, recv_window=recv_window, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> GiftCardWithRawResponse:
        return self._with_raw_response


class AsyncGiftCard:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGiftCardWithRawResponse(client, server, auth)

    async def buy_a_binance_code_trade(
        self,
        base_token: str,
        face_token: str,
        base_token_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardBuyCodeResponse:
        """This API is for buying a fixed-value Binance Code, which means your Binance Code will be redeemable to a
        token that is different to the token that you are paying in. If the token you’re paying and the redeemable token
        are the same, please use the Create Binance Code endpoint. You can use supported crypto currency or fiat token
        as baseToken to buy Binance Code that is redeemable to your chosen faceToken. Once successfully purchased, the
        amount of baseToken would be deducted from your funding wallet.

        To get started with, please make sure:
        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            face_token: The token you want to buy, example BNB. If faceToken = baseToken, it's the same as createCode
                endpoint.
            base_token_amount: The base token asset quantity, example 1.002
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code creation

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.buy_a_binance_code_trade(
                base_token,
                face_token,
                base_token_amount,
                timestamp,
                signature,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def create_a_binance_code_user_data(
        self,
        token: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardCreateCodeResponse:
        """This API is for creating a Binance Code. To get started with, please make sure:

        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            token: The coin type contained in the Binance Code
            amount: The amount of the coin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code creation

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.create_a_binance_code_user_data(
                token, amount, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def fetch_rsa_public_key_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardCryptographyRsaPublicKeyResponse:
        """This API is for fetching the RSA Public Key. This RSA Public key will be used to encrypt the card code.
        Please note that the RSA Public key fetched is valid only for the current day.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            RSA Public Key.

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fetch_rsa_public_key_user_data(
                timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def fetch_token_limit_user_data(
        self,
        base_token: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardBuyCodeTokenLimitResponse:
        """This API is to help you verify which tokens are available for you to purchase fixed-value gift cards as
        mentioned in section 2 and it's limitation.

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Token limit

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.fetch_token_limit_user_data(
                base_token, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    async def redeem_a_binance_code_user_data(
        self,
        code: str,
        timestamp: int,
        signature: str,
        *,
        external_uid: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardRedeemCodeResponse:
        """This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding
        wallet.

        Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any
        Binance Code that day.

        Weight(IP): 1

        Args:
            code: Binance Code
            timestamp: UTC timestamp in ms
            signature: Signature
            external_uid: Each external unique ID represents a unique user on the partner platform. The function helps
                you to identify the redemption behavior of different users, such as redemption frequency and amount. It
                also helps risk and limit control of a single account, such as daily limit on redemption volume,
                frequency, and incorrect number of entries. This will also prevent a single user account reach the
                partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the
                User ID of your users if you have different users redeeming Binance codes on your platform. To protect
                user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters).
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Redeemed Information

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.redeem_a_binance_code_user_data(
                code,
                timestamp,
                signature,
                external_uid=external_uid,
                recv_window=recv_window,
                request_options=request_options,
            )
        ).unwrap()

    async def verify_a_binance_code_user_data(
        self,
        reference_no: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SapiV1GiftcardVerifyResponse:
        """This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference
        number.

        Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to
        verify any binance code for that hour.

        Weight(IP): 1

        Args:
            reference_no: reference number
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Code Verification

        Raises:
            ApiError: Bad Request Unauthorized Request ``error`` is ``Error | RawError``."""
        return (
            await self._with_raw_response.verify_a_binance_code_user_data(
                reference_no, timestamp, signature, recv_window=recv_window, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGiftCardWithRawResponse:
        return self._with_raw_response


class GiftCardWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def buy_a_binance_code_trade(
        self,
        base_token: str,
        face_token: str,
        base_token_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardBuyCodeResponse, BuyABinanceCodeTradeErrorBody]:
        """This API is for buying a fixed-value Binance Code, which means your Binance Code will be redeemable to a
        token that is different to the token that you are paying in. If the token you’re paying and the redeemable token
        are the same, please use the Create Binance Code endpoint. You can use supported crypto currency or fiat token
        as baseToken to buy Binance Code that is redeemable to your chosen faceToken. Once successfully purchased, the
        amount of baseToken would be deducted from your funding wallet.

        To get started with, please make sure:
        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            face_token: The token you want to buy, example BNB. If faceToken = baseToken, it's the same as createCode
                endpoint.
            base_token_amount: The base token asset quantity, example 1.002
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/giftcard/buyCode"),
            query_params=[
                param[str]("baseToken", base_token),
                param[str]("faceToken", face_token),
                param[float]("baseTokenAmount", base_token_amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardBuyCodeResponse],
            error_mapper=buy_a_binance_code_trade_error_mapper,
            request_options=request_options,
        )

    def create_a_binance_code_user_data(
        self,
        token: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardCreateCodeResponse, CreateABinanceCodeUserDataErrorBody]:
        """This API is for creating a Binance Code. To get started with, please make sure:

        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            token: The coin type contained in the Binance Code
            amount: The amount of the coin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/giftcard/createCode"),
            query_params=[
                param[str]("token", token),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardCreateCodeResponse],
            error_mapper=create_a_binance_code_user_data_error_mapper,
            request_options=request_options,
        )

    def fetch_rsa_public_key_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardCryptographyRsaPublicKeyResponse, FetchRsaPublicKeyUserDataErrorBody]:
        """This API is for fetching the RSA Public Key. This RSA Public key will be used to encrypt the card code.
        Please note that the RSA Public key fetched is valid only for the current day.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/giftcard/cryptography/rsa-public-key"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardCryptographyRsaPublicKeyResponse],
            error_mapper=fetch_rsa_public_key_user_data_error_mapper,
            request_options=request_options,
        )

    def fetch_token_limit_user_data(
        self,
        base_token: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardBuyCodeTokenLimitResponse, FetchTokenLimitUserDataErrorBody]:
        """This API is to help you verify which tokens are available for you to purchase fixed-value gift cards as
        mentioned in section 2 and it's limitation.

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/giftcard/buyCode/token-limit"),
            query_params=[
                param[str]("baseToken", base_token),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardBuyCodeTokenLimitResponse],
            error_mapper=fetch_token_limit_user_data_error_mapper,
            request_options=request_options,
        )

    def redeem_a_binance_code_user_data(
        self,
        code: str,
        timestamp: int,
        signature: str,
        *,
        external_uid: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardRedeemCodeResponse, RedeemABinanceCodeUserDataErrorBody]:
        """This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding
        wallet.

        Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any
        Binance Code that day.

        Weight(IP): 1

        Args:
            code: Binance Code
            timestamp: UTC timestamp in ms
            signature: Signature
            external_uid: Each external unique ID represents a unique user on the partner platform. The function helps
                you to identify the redemption behavior of different users, such as redemption frequency and amount. It
                also helps risk and limit control of a single account, such as daily limit on redemption volume,
                frequency, and incorrect number of entries. This will also prevent a single user account reach the
                partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the
                User ID of your users if you have different users redeeming Binance codes on your platform. To protect
                user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters).
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/giftcard/redeemCode"),
            query_params=[
                param[str]("code", code),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("externalUid", external_uid),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardRedeemCodeResponse],
            error_mapper=redeem_a_binance_code_user_data_error_mapper,
            request_options=request_options,
        )

    def verify_a_binance_code_user_data(
        self,
        reference_no: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardVerifyResponse, VerifyABinanceCodeUserDataErrorBody]:
        """This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference
        number.

        Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to
        verify any binance code for that hour.

        Weight(IP): 1

        Args:
            reference_no: reference number
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/giftcard/verify"),
            query_params=[
                param[str]("referenceNo", reference_no),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardVerifyResponse],
            error_mapper=verify_a_binance_code_user_data_error_mapper,
            request_options=request_options,
        )


class AsyncGiftCardWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def buy_a_binance_code_trade(
        self,
        base_token: str,
        face_token: str,
        base_token_amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardBuyCodeResponse, BuyABinanceCodeTradeErrorBody]:
        """This API is for buying a fixed-value Binance Code, which means your Binance Code will be redeemable to a
        token that is different to the token that you are paying in. If the token you’re paying and the redeemable token
        are the same, please use the Create Binance Code endpoint. You can use supported crypto currency or fiat token
        as baseToken to buy Binance Code that is redeemable to your chosen faceToken. Once successfully purchased, the
        amount of baseToken would be deducted from your funding wallet.

        To get started with, please make sure:
        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            face_token: The token you want to buy, example BNB. If faceToken = baseToken, it's the same as createCode
                endpoint.
            base_token_amount: The base token asset quantity, example 1.002
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/giftcard/buyCode"),
            query_params=[
                param[str]("baseToken", base_token),
                param[str]("faceToken", face_token),
                param[float]("baseTokenAmount", base_token_amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardBuyCodeResponse],
            error_mapper=buy_a_binance_code_trade_error_mapper,
            request_options=request_options,
        )

    async def create_a_binance_code_user_data(
        self,
        token: str,
        amount: float,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardCreateCodeResponse, CreateABinanceCodeUserDataErrorBody]:
        """This API is for creating a Binance Code. To get started with, please make sure:

        - You have a Binance account
        - You have passed kyc
        - You have a sufficient balance in your Binance funding wallet
        - You need Enable Withdrawals for the API Key which requests this endpoint.

        Daily creation volume: 2 BTC / 24H Daily creation times: 200 Codes / 24H

        Weight(IP): 1

        Args:
            token: The coin type contained in the Binance Code
            amount: The amount of the coin
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/giftcard/createCode"),
            query_params=[
                param[str]("token", token),
                param[float]("amount", amount),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardCreateCodeResponse],
            error_mapper=create_a_binance_code_user_data_error_mapper,
            request_options=request_options,
        )

    async def fetch_rsa_public_key_user_data(
        self,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardCryptographyRsaPublicKeyResponse, FetchRsaPublicKeyUserDataErrorBody]:
        """This API is for fetching the RSA Public Key. This RSA Public key will be used to encrypt the card code.
        Please note that the RSA Public key fetched is valid only for the current day.

        Weight(IP): 1

        Args:
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/giftcard/cryptography/rsa-public-key"),
            query_params=[
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardCryptographyRsaPublicKeyResponse],
            error_mapper=fetch_rsa_public_key_user_data_error_mapper,
            request_options=request_options,
        )

    async def fetch_token_limit_user_data(
        self,
        base_token: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardBuyCodeTokenLimitResponse, FetchTokenLimitUserDataErrorBody]:
        """This API is to help you verify which tokens are available for you to purchase fixed-value gift cards as
        mentioned in section 2 and it's limitation.

        Weight(IP): 1

        Args:
            base_token: The token you want to pay, example BUSD
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/giftcard/buyCode/token-limit"),
            query_params=[
                param[str]("baseToken", base_token),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardBuyCodeTokenLimitResponse],
            error_mapper=fetch_token_limit_user_data_error_mapper,
            request_options=request_options,
        )

    async def redeem_a_binance_code_user_data(
        self,
        code: str,
        timestamp: int,
        signature: str,
        *,
        external_uid: str | None = None,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardRedeemCodeResponse, RedeemABinanceCodeUserDataErrorBody]:
        """This API is for redeeming the Binance Code. Once redeemed, the coins will be deposited in your funding
        wallet.

        Please note that if you enter the wrong code 5 times within 24 hours, you will no longer be able to redeem any
        Binance Code that day.

        Weight(IP): 1

        Args:
            code: Binance Code
            timestamp: UTC timestamp in ms
            signature: Signature
            external_uid: Each external unique ID represents a unique user on the partner platform. The function helps
                you to identify the redemption behavior of different users, such as redemption frequency and amount. It
                also helps risk and limit control of a single account, such as daily limit on redemption volume,
                frequency, and incorrect number of entries. This will also prevent a single user account reach the
                partner's daily redemption limits. We strongly recommend you to use this feature and transfer us the
                User ID of your users if you have different users redeeming Binance codes on your platform. To protect
                user data privacy, you may choose to transfer the user id in any desired format (max. 400 characters).
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/sapi/v1/giftcard/redeemCode"),
            query_params=[
                param[str]("code", code),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[str | None]("externalUid", external_uid),
                param[int | None]("recvWindow", recv_window),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardRedeemCodeResponse],
            error_mapper=redeem_a_binance_code_user_data_error_mapper,
            request_options=request_options,
        )

    async def verify_a_binance_code_user_data(
        self,
        reference_no: str,
        timestamp: int,
        signature: str,
        *,
        recv_window: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SapiV1GiftcardVerifyResponse, VerifyABinanceCodeUserDataErrorBody]:
        """This API is for verifying whether the Binance Code is valid or not by entering Binance Code or reference
        number.

        Please note that if you enter the wrong binance code 5 times within an hour, you will no longer be able to
        verify any binance code for that hour.

        Weight(IP): 1

        Args:
            reference_no: reference number
            timestamp: UTC timestamp in ms
            signature: Signature
            recv_window: The value cannot be greater than 60000
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/sapi/v1/giftcard/verify"),
            query_params=[
                param[str]("referenceNo", reference_no),
                param[int]("timestamp", timestamp),
                param[str]("signature", signature),
                param[int | None]("recvWindow", recv_window),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SapiV1GiftcardVerifyResponse],
            error_mapper=verify_a_binance_code_user_data_error_mapper,
            request_options=request_options,
        )
