
def return_tonality(escala: str):
    match escala:
        case 'major':
            major = [[0,2,4,5,7,9,11,12], [5]]
            return major
        case 'minor':
            minor = [[0,2,3,5,7,8,10,12], [3]]
            return minor
        case _:
            return TypeError