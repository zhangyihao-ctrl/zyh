#coding=gbk
"""
����: ���RPSLS��Ϸ,RPSLS��Rock-paper-scissors-lizard-Spock��ʯͷ����������ʷ����
����:���պ�
����:2019��11��20��
"""

import random#����random����
comp_number=random.randint(0,5)



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="ֽ":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error: No Correct Name")
"""
����Ϸ�����Ӧ����ͬ������
"""

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��

def number_to_name(comp_number):
	if comp_number==0:
		return "ʯͷ"
	elif comp_number==1:
		return "ʷ����"
	elif comp_number==2:
		return "ֽ"
	elif comp_number==3:
		return "����"
	elif comp_number==4:
		return "����"
	return(comp_number)
"""
������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
"""

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��


def rpsls(player_choice):
	player_choice=name_to_number(choice_name)
	if player_choice==comp_number:
		print("���ͼ��������һ����")
	elif player_choice==0 and comp_number==1:
		print("�����Ӯ��")
	elif player_choice==0 and comp_number==2:
		print("�����Ӯ��")
	elif player_choice==0 and comp_number==3:
		print("��Ӯ��")
	elif player_choice==0 and comp_number==4:
		print("��Ӯ��")
	elif player_choice==1 and comp_number==0:
		print("��Ӯ��")
	elif player_choice==1 and comp_number==2:
		print("�����Ӯ��")
	elif player_choice==1 and comp_number==3:
		print("�����Ӯ��")
	elif player_choice==1 and comp_number==4:
		print("��Ӯ��")
	elif player_choice==2 and comp_number==0:
		print("��Ӯ��")
	elif player_choice==2 and comp_number==1:
		print("��Ӯ��")
	elif player_choice==2 and comp_number==3:
		print("�����Ӯ��")
	elif player_choice==2 and comp_number==4:
		print("�����Ӯ��")
	elif player_choice==3 and comp_number==0:
		print("�����Ӯ��")
	elif player_choice==3 and comp_number==1:
		print("��Ӯ��")
	elif player_choice==3 and comp_number==2:
		print("��Ӯ��")
	elif player_choice==3 and comp_number==4:
		print("�����Ӯ��")
	elif player_choice==4 and comp_number==0:
		print("�����Ӯ��")
	elif player_choice==4 and comp_number==1:
		print("�����Ӯ��")
	elif player_choice==4 and comp_number==2:
		print("��Ӯ��")
	elif player_choice==4 and comp_number==3:
		print("��Ӯ��")
"""
�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
"""


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
comp_choice=number_to_name(comp_number)
print("�������ѡ��Ϊ",comp_choice)
rpsls(choice_name)
