import csv

def count_votes(file_path):
    results = {}
    
    with open(file_path, newline='') as csvfile:
        data_votaciones = csv.reader(csvfile, delimiter=',')
        next(data_votaciones)  # Skip the header

        for row in data_votaciones:
            candidate = row[1]
            try:
            	votes = int(row[2])
            except:
                votes = 0
            
            results[candidate] = results.get(candidate, 0) + votes

    print_of_candidates_and_winner(results)



def print_of_candidates_and_winner(results):
    for candidate, total_votes in results.items():
        print(f"{candidate}: {total_votes} votes")

    sortedbyvotes = sorted(results.items(), key=lambda item:item[1], reverse=True)
    primer_mas_votado=sortedbyvotes[0][1]
    segundo_mas_votado=sortedbyvotes[1][1]
    if(primer_mas_votado==segundo_mas_votado):
        print(f"Existe empate, no hay ganador")
        return
    print(f"winner is {sortedbyvotes[0][0]}")
# Example usage
count_votes('votes.csv')
