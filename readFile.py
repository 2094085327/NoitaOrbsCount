import config
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import xml.etree.ElementTree as Et
import xml.dom.minidom


def decryption(data):
    # 密钥和IV的值
    key = bytes.fromhex(config.key)
    iv = bytes.fromhex(config.iv)

    # 创建AES-CTR密码器
    cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    return decryptor.update(data) + decryptor.finalize()


# 读取session加密文件
def readSalakieli():
    with open(config.save00Path + "\\save00\\session_numbers.salakieli", "rb") as file:
        data = file.read()
        decryption_content = decryption(data)
        return decryption_content


def getWorldPlusNum():
    # 获取根元素
    root = Et.fromstring(readSalakieli())

    # 找到NEW_GAME_PLUS_COUNT获取这是第几个新世间
    return root.get("NEW_GAME_PLUS_COUNT")


# 获取当前周目已获得的魔球数
def getOrbsNum():
    # 解析XML文件
    tree = Et.parse(config.save00Path + "\\save00\\world_state.xml")

    # 获取根元素
    root = tree.getroot()

    # 找到<WorldStateComponent>元素
    worldStateComponent = root.find(".//WorldStateComponent")

    # 找到<orbs_found_thisrun>元素
    orbsFoundThisRun = worldStateComponent.find("orbs_found_thisrun")

    return len(list(orbsFoundThisRun))
