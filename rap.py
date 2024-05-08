# import pyttsx3
# # 辅助函数，将数字转换为对应的英文单词
# def number_to_word(number):
#     #numbers_to_words = {
#     #    1: '哟',
#     #    2: '欸',
#     #    3: '嘿',
#     #    4: '吼',
#     #    5: '呼',
#     #    6: '撒',
#     #    7: '瑟',
#     #    8: '呀',
#     #    9: '哦'
#     #}
#     numbers_to_words = {
#         1: 'sun',
#         2: 'crew',
#         3: 'see',
#         4: 'door',
#         5: 'hive',
#         6: 'sticks',
#         7: 'heaven',
#         8: 'gate',
#         9: 'line'
#     }
#     return numbers_to_words.get(number, '')  # 如果数字不在字典中，返回空字符串
# def count_and_say(n):
#     result = '1'
#     for _ in range(1, n):
#         repeat_count = 1
#         output = ''
#         for j in range(len(result)):
#             if j < len(result) - 1 and result[j] == result[j + 1]:
#                 repeat_count += 1
#             else:
#                 output += str(repeat_count) + result[j]
#                 repeat_count = 1
#         result = output
#     return result

# # 设置语音引擎
# engine = pyttsx3.init()

# # 获取序列的第n个元素
# for n in range(1,101):
#     sequence = count_and_say(n)

#     # 将结果转换为语音
#     spoken_sequence = ''
#     for char in sequence:
#         if char.isdigit():
#             spoken_sequence += f"{number_to_word(int(char))} "

#     spoken_sequence = spoken_sequence.strip()

#     # 输出结果到控制台
#     print(spoken_sequence)

#     # 将结果转换为语音
#     engine.say(spoken_sequence)
#     engine.runAndWait()

# import pyttsx3
# import random

# # 辅助函数，将数字转换为对应的英文单词
# def number_to_word(number):
#     rap_vocabulary = {
#         1: 'one, sun',
#         2: 'two, crew',
#         3: 'three, see',
#         4: 'four, floor',
#         5: 'five, thrive',
#         6: 'six, sticks',
#         7: 'seven, in heaven',
#         8: 'eight, straight',
#         9: 'nine, line'
#     }
#     return rap_vocabulary.get(number, '')  # 如果数字不在字典中，返回空字符串

# def count_and_say(n):
#     result = '1'
#     for _ in range(1, n):
#         repeat_count = 1
#         output = ''
#         for j in range(len(result)):
#             if j < len(result) - 1 and result[j] == result[j + 1]:
#                 repeat_count += 1
#             else:
#                 output += str(repeat_count) + result[j]
#                 repeat_count = 1
#         result = output
#     return result

# # 设置语音引擎
# engine = pyttsx3.init()

# # 获取序列的第n个元素
# for n in range(1, 101):
#     sequence = count_and_say(n)

#     # 将结果转换为语音
#     spoken_sequence = ''
#     for char in sequence:
#         if char.isdigit():
#             spoken_sequence += f"{random.choice(number_to_word(int(char)).split(', '))} "

#     spoken_sequence = spoken_sequence.strip()

#     # 输出结果到控制台
#     print(spoken_sequence)

#     # 将结果转换为语音
#     engine.say(spoken_sequence)
#     engine.runAndWait()

# import pyttsx3
# import random

# # 辅助函数，将数字转换为对应的英文单词
# def number_to_word(number):
#     rap_vocabulary = {
#         1: ["Yo, it's the rap that I bring, with a beat that makes you swing"],
#         2: ["Check it, the numbers they flow, like a river down low"],
#         3: ["Listen up, to the words I say, it's the count and say all day"],
#         4: ['four'],
#         5: ['five'],
#         6: ['six'],
#         7: ['seven'],
#         8: ['eight'],
#         9: ['nine']
#     }
#     return random.choice(rap_vocabulary.get(number, ['']))  # 如果数字不在字典中，返回空字符串

# # 创建一个押韵的叠句
# def rhyming_couplet():
#     rhymes = [
#         "Yo, it's the rap that I bring, with a beat that makes you swing",
#         "Check it, the numbers they flow, like a river down low",
#         "Listen up, to the words I say, it's the count and say all day",
#         "In the mix, with the digits, it's the rap that fits the picture"
#     ]
#     return random.choice(rhymes)

# # 设置语音引擎
# engine = pyttsx3.init()

# # 获取序列的第n个元素
# for n in range(1, 11):  # 为了演示，只生成前10个序列
#     sequence = count_and_say(n)

#     # 将结果转换为语音
#     spoken_sequence = ''
#     for char in sequence:
#         if char.isdigit():
#             spoken_sequence += f"{number_to_word(int(char))} "

#     spoken_sequence = spoken_sequence.strip()

#     # 添加押韵的叠句
#     rap_line = f"{spoken_sequence}, {rhyming_couplet()}"

#     # 输出结果到控制台
#     print(rap_line)

#     # 将结果转换为语音
#     engine.say(rap_line)
#     engine.runAndWait()

# import pyttsx3
# import random
# import time
# # 辅助函数，将数字转换为对应的英文单词
# def number_to_word(number):
#     numbers_to_words = {
#         1: 'sun',
#         2: 'crew',
#         3: 'see',
#         4: 'door',
#         5: 'hive',
#         6: 'sticks',
#         7: 'heaven',
#         8: 'gate',
#         9: 'line'
#     }
#     return numbers_to_words.get(number, '')  # 如果数字不在字典中，返回空字符串

# def count_and_say(n):
#     result = '1'
#     for _ in range(1, n):
#         repeat_count = 1
#         output = ''
#         for j in range(len(result)):
#             if j < len(result) - 1 and result[j] == result[j + 1]:
#                 repeat_count += 1
#             else:
#                 output += str(repeat_count) + result[j]
#                 repeat_count = 1
#         result = output
#     return result

# # 设置语音引擎
# engine = pyttsx3.init()

# # 设置语速
# engine.setProperty('rate', 150)  # 调整语速

# # 获取序列的第n个元素
# for n in range(1, 11):  # 只做前10个元素的演示
#     sequence = count_and_say(n)

#     # 将结果转换为语音
#     spoken_sequence = ''
#     for char in sequence:
#         if char.isdigit():
#             spoken_sequence += f"{number_to_word(int(char))} "
#         else:
#             spoken_sequence += char  # 保持其他字符不变

#     spoken_sequence = spoken_sequence.strip()

#     # 输出结果到控制台
#     print(spoken_sequence)

#     # 将结果转换为语音，并加入随机停顿
#     for word in spoken_sequence.split():
#         engine.say(word)
#         engine.runAndWait()
#         # 在每个词之间加入随机长度的停顿
#         engine.say('')  # 空白词以产生停顿
#         engine.runAndWait()
#         random_pause = random.uniform(0.1, 0.5)  # 随机停顿时间
#         time.sleep(random_pause)

# # 注意：为了听到背景音乐，您可能需要在您的操作系统中播放音乐，或者使用Python的其他库来处理音频。

# import pyttsx3

# dict = {
#         1: 'sun',
#         2: 'crew',
#         3: 'see',
#         4: 'door',
#         5: 'hive',
#         6: 'sticks',
#         7: 'heaven',
#         8: 'gate',
#         9: 'line'
#     }
# # 辅助函数，将数字转换为对应的英文单词
# def number_to_word(number):
#     numbers_to_words = {
#         1: '1',
#         2: '2',
#         3: '3',
#         4: '4',
#         5: '5',
#         6: '6',
#         7: '7',
#         8: '8',
#         9: '9'
#     }
#     return numbers_to_words.get(number, '')  # 如果数字不在字典中，返回空字符串

# def count_and_say(n):
#     result = '1'
#     for _ in range(1, n):
#         repeat_count = 1
#         output = ''
#         for j in range(len(result)):
#             if j < len(result) - 1 and result[j] == result[j + 1]:
#                 repeat_count += 1
#             else:
#                 output += str(repeat_count) + result[j]
#                 repeat_count = 1
#         result = output
#     return result

# # 设置语音引擎
# engine = pyttsx3.init()

# # 设置默认语速
# default_rate = 150
# engine.setProperty('rate', default_rate)

# # 获取序列的第n个元素
# for n in range(1, 11):  # 只做前10个元素的演示
#     sequence = count_and_say(n)

#     # 将结果转换为语音
#     spoken_sequence = ''
#     for char in sequence:
#         if char.isdigit():
#             spoken_sequence += f"{number_to_word(int(char))} "
#         else:
#             spoken_sequence += char  # 保持其他字符不变

#     spoken_sequence = spoken_sequence.strip()

#     # 输出结果到控制台
#     print(spoken_sequence)

#     # 将结果转换为语音，并调整语速
#     words = spoken_sequence.split()
#     print(words)

#     for i, word in enumerate(words):
#         if word:
#             # 如果下一个词也是相同的数字，增加语速
#             if i < len(words) - 1 and word == words[i + 1]:
#                 engine.setProperty('rate', default_rate * 1.5 * int(word))  # 增加语速
#                 print("aaaaaaaaaaaaaaaaaa")
#             else:
#                 engine.setProperty('rate', default_rate)  # 恢复默认语速
#         engine.say(dict[int(word)])
#         engine.runAndWait()

# 注意：为了听到背景音乐，您可能需要在您的操作系统中播放音乐，或者使用Python的其他库来处理音频。

import pyttsx3
import random
import math
# 数字到单词的映射
dict = {
        1: 'sun',
        2: 'crew',
        3: 'see',
        4: 'door',
        5: 'hive',
        6: 'sticks',
        7: 'heaven',
        8: 'gate',
        9: 'line'
}
dict2 = {
        'sun':1,
        'crew':2,
        'see':3,
        'door':4,
        'hive':5,
        'sticks':6,
        'heaven':7,
        'gate':8,
        'line':9
}

# 辅助函数，将数字转换为对应的英文单词
def number_to_word(number):
    return dict.get(number, '')  # 如果数字不在字典中，返回空字符串

def count_and_say(n):
    result = '1'
    for _ in range(1, n):
        repeat_count = 1
        output = ''
        for j in range(len(result)):
            if j < len(result) - 1 and result[j] == result[j + 1]:
                repeat_count += 1
            else:
                output += str(repeat_count) + result[j]
                repeat_count = 1
        result = output
    return result

# 设置语音引擎
engine = pyttsx3.init()

# 设置默认语速
default_rate = 150
engine.setProperty('rate', default_rate)

# 获取序列的第n个元素
for n in range(1, 30):  # 只做前10个元素的演示
    sequence = count_and_say(n)

    # 将结果转换为语音
    spoken_sequence = ''
    for char in sequence:
        if char.isdigit():
            spoken_sequence += f"{number_to_word(int(char))} "
        else:
            spoken_sequence += char  # 保持其他字符不变

    spoken_sequence = spoken_sequence.strip()

    # 输出结果到控制台
    print(spoken_sequence)

    # 将结果转换为语音，并调整语速和停顿时间
    words = spoken_sequence.split()
    for i, word in enumerate(words):
        if word:
            # 根据数字的值来决定是否插入语气助词
            a = 0
            b = 0
            if i < len(words) - 1 and word == words[i + 1]:
                # 如果下一个词也是相同的数字，增加语速并插入无声语气助词
                a = 2
                for i in range(int(dict2[word])):
                    a *= 2
                engine.setProperty('rate', default_rate * a)
                b = 2
                for i in range(int(dict2[word])):
                    b *= 2
                word += '\u200c' * b # 零宽度非连接符，不会发音
            else:
                engine.setProperty('rate', default_rate)
        temp = ''
        for i in range(random.randint(3, 12)):
            temp += word + dict[random.randint(1, 9)]*random.randint(1, 3) + word
        engine.say(temp)
        engine.runAndWait()
        # 打乱字典的键
        keys = list(dict.keys())
        random.shuffle(keys)

        # 创建新的轮换字典
        dict = {key: dict[keys[key-1]] for key in keys}
    default_rate += 15
# 注意：为了听到背景音乐，您可能需要在您的操作系统中播放音乐，或者使用Python的其他库来处理音频。
