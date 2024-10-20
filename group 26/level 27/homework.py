#is_anagram("foefet", "toffee") -> True
#is_anagram("Buckethead", "DeathCubeK") -> True
#is_anagram("Twoo", "WooT") -> True
#is_anagram("apple", "pale") -> False

def is_anagram(test, original):
    # სტრიქონების ნორმალიზაცია
    test = test.lower()
    original = original.lower()

    # სორტირება და შედარება
    return sorted(test) == sorted(original)
