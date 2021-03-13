import requests, random

if __name__ == '__main__':
    email = input("Enter Your Email: ")
    r = requests.get('https://shortrndexercise.singular.net/get-key?email={}'.format(email))
    json = r.json()
    P = json.get('p')
    G = json.get('g')
    A_PUBLIC = json.get('A_public')
    print("Th P is {} ||| G is {} ||| A_PUBLIC is {} ".format(P, G, A_PUBLIC))
    PRIVATE_NUMBER = random.randint(11111111111111111111111111,225352523525223532525252525225255225525252)
    B_PUBLIC = int(pow(G, PRIVATE_NUMBER, P))
    print("B_PUBLIC:", B_PUBLIC)
    SOLUTION = int(pow(A_PUBLIC, PRIVATE_NUMBER, P))
    r_v2 = requests.get("https://shortrndexercise.singular.net/submit?email={}&B_public={}&solution={}".format(email, B_PUBLIC, SOLUTION))
    json_v2 = r_v2.json()
    print("Final Response: ", json_v2)
