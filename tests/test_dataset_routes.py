"""Test the /datasets blueprint routes."""

import json

from . import tmp_app, tmp_app_with_data, tmp_app_with_users  # NOQA


snowwhite_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyZTk0MzMzMi0wZWE5LTQ3MWMtYTUxZS02MjUxNGNlOTdkOGMiLCJmcmVzaCI6ZmFsc2UsImlhdCI6MTU1MzI2NTM5NywidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU1MzI2NTM5NywiaWRlbnRpdHkiOiJzbm93LXdoaXRlIn0.FAoj9M4Tpr9IXIsyuD9eKV3oOpQ4_oRE82v6jqMFOSERaMqfWQgpMlTPSBsoWvnsNhigBYA7NKqqRPZ_bCHh73dMk57s6-VBvxtunQIe-MYtnOP9H4lpIdnceIE-Ji34xCd7kxIp0kADtYLhnJjU6Jesk642P0Ndjc8ePxGAl-l--bLbH_A4a3-U2EuowBSwqAp2q56QuGw6oQpKSKt9_eRSThNBE6zJIClfUeQYeCDCcd1Inh5hgrDBurteicCP8gWyVkyZ0YnjojDMECu7P9vDyy-T4AUem9EIAe_hA1nTMKucW2Ki6xyZLvu0TVlHe9AQVYy0O-suxxlrXIJ5Yw"  # NOQA

grumpy_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI5NjJjODEyNi1kZDJlLTQ1NDEtODQyOC0yZDYxYjEwZmU0M2YiLCJmcmVzaCI6ZmFsc2UsImlhdCI6MTU1MzIyMzEzMywidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU1MzIyMzEzMywiaWRlbnRpdHkiOiJncnVtcHkifQ.K1YYcUp2jfpBhVd7ggBJ_mpnQT_ZAGRjfgrReoz9no6zZ_5Hlgq2YLUNFtFfr2PrqsaO5fKWUfKrR8bjMijtlRlAEmyCJvalqXDWvriMf2QowyR6IjKxSNZcVCMkJXEk7cRlEM9f815YABc3RsG1F75n2dV5NSuvcQ4dQoItvNYpsuHZ3c-xYQuaQt7_Ch50Ez-H2fJatXQYdnHruyZOJQKPIssxU_yyeCnlOGklCmDn8mIolQEChrvW9HhpvgXsaAWEHjtNRK4T_ZH37Dq44fIB9ax6GGRZHDjWmjOicrGolfu73BuI8fOpLLpW5af6SKP-UhZA4AcW_TYG4PnOpQ"  # NOQA

sleepy_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhNzBhNmQ1ZS0xMTU4LTQ5YzAtOGM0OS02MmU1MzYzZWM3NDQiLCJmcmVzaCI6ZmFsc2UsImlhdCI6MTU1MzIyMzIyNCwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU1MzIyMzIyNCwiaWRlbnRpdHkiOiJzbGVlcHkifQ.o15vGkZVsP_RaCIwXljFrkmFTef7ToPo_ssg7DPzRc33LhZh352gn6kY90JGMD1eyvrw69u6RwKW_5RkBmkDweCExiSDx7EuEofgadEegkM9qfbRfPGRpihobmQmwDADc6qspROUDi__gjrALLFZvg8cAteBVOBhKrItwHADym4RCHzDTyP0dd-k8PzvKUqBxryK5yutpc5Tkju3Bg33bFIyjJTr9kzZbjnzoYSjl1Nb7YtCO6ijsJasIPfLK8OOB2kza9NrAOAhWKqWtynzkyCCVckicfGZI5ywzNlsUqGcQwb7fNMUR-1JErM0wGViKOmotcQ08ut69KM5p8XZmg"  # NOQA

dopey_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI0MTIxZDhhYi1iYjg5LTRlYTgtOTg3Zi0zYjgyOTc2ODkwZjEiLCJmcmVzaCI6ZmFsc2UsImlhdCI6MTU1MzIyMzM0MCwidHlwZSI6ImFjY2VzcyIsIm5iZiI6MTU1MzIyMzM0MCwiaWRlbnRpdHkiOiJkb3BleSJ9.K8MeDodbdwDN2ErspmWgQJCra3EXdpIrsyWQVqCNZNKsjUZsYLNAetzqJe71NhiVFuoaqDm0ta9jNnQE5NpehQSFv0SveMPu4wIaVpcCDQXHOYGGljbhHa18v0dEZibZFEYnMwY_b0VWtpzXZXZSYiLVMD2kcnUqXouV7fPXlSp5SuFCEh5Y6rw0nZqxMTVdbDvZLm2rxjJI_4GHMj1KMpsGKYGTxniA1iWvR9WionJOdDxn5gc8roDERGuSQpm4LCQxz_WJk8pNX4IdQgPuz6TVNsXnUnD2LiGe9Dz8q-FstcTwRy2u97l76OgCGSf7vkhELHTqRj32cEdxnPNpTA"  # NOQA


def test_dataset_list_route(tmp_app_with_data):  # NOQA

    headers = dict(Authorization="Bearer " + grumpy_token)
    r = tmp_app_with_data.get(
        "/dataset/list",
        headers=headers
    )
    assert r.status_code == 200

    assert len(json.loads(r.data)) == 3

    r = tmp_app_with_data.get(
        "/dataset/list",
        headers=dict(Authorization="Bearer " + sleepy_token)
    )
    assert r.status_code == 200
    assert json.loads(r.data) == []

    r = tmp_app_with_data.get(
        "/dataset/list",
        headers=dict(Authorization="Bearer " + dopey_token)
    )
    assert r.status_code == 401


def test_dataset_search_route(tmp_app_with_data):  # NOQA

    headers = dict(Authorization="Bearer " + grumpy_token)
    query = {}  # Everything.
    r = tmp_app_with_data.post(
        "/dataset/search",
        headers=headers,
        data=json.dumps(query),
        content_type="application/json"
    )
    assert r.status_code == 200

    assert len(json.loads(r.data)) == 3

    r = tmp_app_with_data.post(
        "/dataset/search",
        headers=dict(Authorization="Bearer " + sleepy_token),
        data=json.dumps(query),
        content_type="application/json"
    )
    assert r.status_code == 200
    assert len(json.loads(r.data)) == 0

    r = tmp_app_with_data.get(
        "/dataset/list",
        headers=dict(Authorization="Bearer " + dopey_token),
        data=json.dumps(query),
        content_type="application/json"
    )
    assert r.status_code == 401

    # Search for apples.
    headers = dict(Authorization="Bearer " + grumpy_token)
    query = {"$text": {"$search": "apple"}}
    r = tmp_app_with_data.post(
        "/dataset/search",
        headers=headers,
        data=json.dumps(query),
        content_type="application/json"
    )
    assert r.status_code == 200

    assert len(json.loads(r.data)) == 2


def test_dataset_register_route(tmp_app_with_users):  # NOQA

    from dtool_lookup_server.utils import (
        get_admin_metadata_from_uri,
        get_readme_from_uri,
        lookup_datasets_by_user_and_uuid,
    )

    base_uri = "s3://snow-white"
    uuid = "af6727bf-29c7-43dd-b42f-a5d7ede28337"
    uri = "{}/{}".format(base_uri, uuid)
    dataset_info = {
        "base_uri": base_uri,
        "uuid": uuid,
        "uri": uri,
        "name": "my-dataset",
        "type": "dataset",
        "readme": {"description": "test dataset"},
    }

    for token in [dopey_token, sleepy_token]:
        headers = dict(Authorization="Bearer " + sleepy_token)
        r = tmp_app_with_users.post(
            "/dataset/register",
            headers=headers,
            data=json.dumps(dataset_info),
            content_type="application/json"
        )
        assert r.status_code == 401

    headers = dict(Authorization="Bearer " + grumpy_token)
    r = tmp_app_with_users.post(
        "/dataset/register",
        headers=headers,
        data=json.dumps(dataset_info),
        content_type="application/json"
    )
    assert r.status_code == 201

    assert get_readme_from_uri(uri) == dataset_info["readme"]

    expected_content = {
        "base_uri": base_uri,
        "uuid": uuid,
        "uri": uri,
        "name": "my-dataset",
    }
    assert get_admin_metadata_from_uri(uri) == expected_content

    assert len(lookup_datasets_by_user_and_uuid("grumpy", uuid)) == 1

    # Add the same dataset again, but with updated readme info.
    dataset_info = {
        "base_uri": base_uri,
        "uuid": uuid,
        "uri": uri,
        "name": "my-dataset",
        "type": "dataset",
        "readme": {"description": "new metadata"},
    }
    r = tmp_app_with_users.post(
        "/dataset/register",
        headers=headers,
        data=json.dumps(dataset_info),
        content_type="application/json"
    )
    assert r.status_code == 201

    assert get_readme_from_uri(uri) == dataset_info["readme"]
    assert get_admin_metadata_from_uri(uri) == expected_content
    assert len(lookup_datasets_by_user_and_uuid("grumpy", uuid)) == 1
