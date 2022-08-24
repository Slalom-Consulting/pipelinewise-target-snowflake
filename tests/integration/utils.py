import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_db_config():
    config = {'account': os.environ.get('TARGET_SNOWFLAKE_ACCOUNT')}

    config['dbname'] = os.environ.get('TARGET_SNOWFLAKE_DBNAME')
    config['user'] = os.environ.get('TARGET_SNOWFLAKE_USER')
    config['password'] = os.environ.get('TARGET_SNOWFLAKE_PASSWORD')
    config['warehouse'] = os.environ.get('TARGET_SNOWFLAKE_WAREHOUSE')
    config['default_target_schema'] = os.environ.get("TARGET_SNOWFLAKE_SCHEMA")
    config['stage'] = os.environ.get("TARGET_SNOWFLAKE_STAGE")
    config['file_format'] = os.environ.get("TARGET_SNOWFLAKE_FILE_FORMAT")

    # AWS IAM and S3 bucket
    config['aws_access_key_id'] = os.environ.get('TARGET_SNOWFLAKE_AWS_ACCESS_KEY')
    config['aws_secret_access_key'] = os.environ.get('TARGET_SNOWFLAKE_AWS_SECRET_ACCESS_KEY')
    config['s3_bucket'] = os.environ.get('TARGET_SNOWFLAKE_S3_BUCKET')
    config['s3_key_prefix'] = os.environ.get('TARGET_SNOWFLAKE_S3_KEY_PREFIX')
    config['s3_acl'] = os.environ.get('TARGET_SNOWFLAKE_S3_ACL')

    # External stage in snowflake with client side encryption details
    config['client_side_encryption_master_key'] = os.environ.get('CLIENT_SIDE_ENCRYPTION_MASTER_KEY')

    # --------------------------------------------------------------------------
    # The following variables needs to be empty.
    # The tests cases will set them automatically whenever it's needed
    # --------------------------------------------------------------------------
    config['disable_table_cache'] = None
    config['schema_mapping'] = None
    config['add_metadata_columns'] = None
    config['hard_delete'] = None
    config['flush_all_streams'] = None
    config['validate_records'] = None

    return config


def get_test_config():
    return get_db_config()


def get_test_tap_lines(filename):
    lines = []
    with open(f'{os.path.dirname(__file__)}/resources/{filename}') as tap_stdout:
        lines.extend(iter(tap_stdout))
    return lines
