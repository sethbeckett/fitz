import openai

def set_key(api_key: str) -> None:
    """
    Sets the OpenAI API key.

    Parameters
    ----------
    api_key : str
        The OpenAI API key to use for requests.

    Returns
    -------
    None
    """
    openai.api_key = api_key

def get_account_info() -> dict:
    """
    Retrieve information about the OpenAI account, including the number of tokens remaining.

    Returns:
        dict: The account information.

    Raises:
        Exception: If there is an error retrieving the account information.
    """
    try:
        account_info = openai.Account.retrieve()
        return account_info
    except Exception as e:
        raise Exception("Error retrieving account information: " + str(e))

    def add_coding_context(directory: str = '.') -> None:
        """
        Changes the configuration's coding context directory and files to the file(s) specified.

        Parameters
        ----------
        directory : str
            The directory that should be added to give the model context. Files inside the directory are all added recursively.

        Returns
        -------
        None
        """
        pass

    def set_model(model_name: str) -> None:
        """
        Sets the model used in the API call. To see current model options, run `openai api models.list` in the terminal

        Parameters
        ----------
        directory : str
            The directory that should be added to give the model context. Files inside the directory are all added recursively.

        Returns
        -------
        None
        """
        pass
