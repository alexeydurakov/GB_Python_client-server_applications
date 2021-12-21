import yaml
from yaml.loader import SafeLoader

with open('data_read.yaml') as f_n:
    f_n_content = yaml.load(f_n, Loader=SafeLoader)
print(f_n_content)

# Результат:
# [{'to': 'account_1', 'action': 'msg_1'}, {'to': 'account_2', 'action': 'msg_2'}]

# Запись данных

action_list = ['msg_1',
          'msg_2',
          'msg_3']

to_list = ['account_1',
      'account_2',
      'account_3']

data_to_yaml = {'action':action_list, 'to':to_list}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n)

with open('data_write.yaml') as f_n:
    print(f_n.read())

# action:
# - msg_1
# - msg_2
# - msg_3
# to:
# - account_1
# - account_2
# - account_3

# Итоговые списки записались в строку. Такой вариант представления определяется по умолчанию. Чтобы его изменить,
# необходимо установить для параметра default_flow_style значение False

action_list = ['msg_1',
          'msg_2',
          'msg_3']

to_list = ['account_1',
      'account_2',
      'account_3']

data_to_yaml = {'action':action_list, 'to':to_list}

with open('data_write.yaml', 'w') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=True)

with open('data_write.yaml') as f_n:
    print(f_n.read())

# а если True то результат
# {action: [msg_1, msg_2, msg_3], to: [account_1, account_2, account_3]}




