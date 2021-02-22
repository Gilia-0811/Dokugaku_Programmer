# http://tinyurl.com/hkzgqrv

def convert(string) :
    """ Converts passed in str to int.
    :param string : str.
    :return : string converted to int.
    """
    try :
        converted = float(string)
        print(converted)
    except ValueError :
        print("float型に変換できません")

convert("gilia")
convert(10)
