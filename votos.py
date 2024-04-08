
def voting_system():
    num_voters = int(input("Informe o número de colaboradores que irão participar da votação: "))
    # Possible days for the vote
    days = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
    # Dictionary to hold the votes for each day
    vote_count = {day: 0 for day in days}
    
    # Ask each voter for their preferred day
    for _ in range(num_voters):
        while True:
            vote = input("Informe o dia da semana de sua preferência para a live (segunda-feira a sexta-feira): ").strip().lower()
            if vote in days:
                vote_count[vote] += 1
                break
            else:
                print("Dia inválido. Por favor, escolha entre segunda-feira e sexta-feira.")
    
    # Find the day with the most votes
    max_votes = max(vote_count.values())
    chosen_day = [day for day, votes in vote_count.items() if votes == max_votes]
    
    return chosen_day, max_votes

voting_results = voting_system()
print(f"O dia escolhido foi: {voting_results[0]} com {voting_results[1]} votos.")