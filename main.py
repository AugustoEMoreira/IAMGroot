import json
import argparse


def get_json_file(file_path):
    with open(file_path) as j:
        return json.load(j)


def get_policy_actions(policy):
    statements = policy['Statement']
    actions = []
    for statement in statements:
        for action in statement['Action']:
            actions.append(action)
    return actions


def search_arr(arr, term):
    for a in arr:
        aux_dict = {k.lower():v for k, v in d.items()}
        aux_term = term.lower()
        if aux_term in aux_dict:
            return aux_dict.get(aux_term)


def get_aws_services_actions(service_name, action_name):
    actions = get_json_file('services/actions.json')
    action_url = f'https://console.aws.amazon.com/iam/api/services/{service_name}/actions/{action_name}'
    x = search_arr(actions, action_url)
    print(x)


def main():
    parser = argparse.ArgumentParser(description="A simple tool to analyze big IAM policies")
    parser.add_argument('path', metavar='PATH', type=str, help='path to JSON')
    args = parser.parse_args()
    policy = get_json_file(args.path)
    policy_actions = get_policy_actions(policy)

    for pa in policy_actions:
        pac = pa.split(':')
        service_name = pac[0]
        action_name = pac[1]
        get_aws_services_actions(service_name, action_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
