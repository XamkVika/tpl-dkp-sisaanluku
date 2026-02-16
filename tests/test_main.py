import pytest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os
import json

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import main

import pytest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os
import json

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import main

@patch('main.pd.DataFrame')
@patch('main.fetch_data')
@patch('main.validate_items')
def test_main_success(mock_validate, mock_fetch, mock_df_class):
    # Mock data
    mock_data = [{'id': 1, 'title': 'Test'}]
    mock_fetch.return_value = mock_data
    mock_validate.return_value = True
    
    # Mock DataFrame instance
    mock_df_instance = MagicMock()
    mock_df_class.return_value = mock_df_instance
    mock_df_instance.to_json = MagicMock(side_effect=lambda path, **kwargs: json.dump(mock_data, open(path, 'w'), indent=4))

    main()

    # Check calls
    mock_fetch.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")
    mock_validate.assert_called_once_with(mock_data)
    mock_df_class.assert_called_once_with(mock_data)
    mock_df_instance.to_json.assert_called_once_with("data/test_posts.json")
    
    # Validate the JSON file exists and contains data
    assert os.path.exists("data/test_posts.json")
    with open("data/test_posts.json", 'r') as f:
        content = json.load(f)
        assert content == mock_data

@patch('main.fetch_data')
@patch('main.validate_items')
def test_main_fetch_fails(mock_validate, mock_fetch):
    mock_fetch.return_value = None

    main()

    mock_fetch.assert_called_once()
    mock_validate.assert_not_called()