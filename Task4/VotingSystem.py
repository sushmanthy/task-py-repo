votes = {'Alice': 0, 'Bob': 0, 'Carol': 0}  # {candidate: count}

def add_vote(candidate):
    candidate = candidate.title()  # Normalize: alice → Alice
    if candidate in votes:
        votes[candidate] += 1
        print(f"✅ Voted for {candidate} (total: {votes[candidate]})")
    else:
        print("❌ Invalid candidate")

def display_results():
    if not votes or sum(votes.values()) == 0:
        print("No votes yet")
        return
    winner = max(votes, key=votes.get)
    total_votes = sum(votes.values())
    print(f"\n{'='*40}")
    print("ELECTION RESULTS")
    print(f"{'='*40}")
    for cand, count in votes.items():
        pct = (count / total_votes) * 100
        print(f"{cand:<10}: {count:>3} votes ({pct:>5.1f}%)")
    print(f"{'='*40}")
    print(f"🏆 WINNER: {winner} ({votes[winner]} votes)")
    print(f"{'='*40}")

# Interactive voting
while True:
    print("\nCandidates: " + ', '.join(votes.keys()))
    candidate = input("Vote (or 'results' or 'quit'): ")
    if candidate.lower() == 'quit':
        break
    elif candidate.lower() == 'results':
        display_results()
    else:
        add_vote(candidate)