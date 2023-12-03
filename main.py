
def count_batteries_by_health(present_capacities):
  #initialize counts for each battery health category
  counts = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }
  #Loop through each battery's present capacity
  for capacity in present_capacities:
    #Calculate the State of Health as a percentage
    soh=(capacity/120)*100
    #Classify the battery based on SoH and update counts
    if soh>80:
      counts["healthy"]+=1
    elif 62<=soh<=80:
      counts["exchange"]+=1
    else:
      counts["failed"]+=1
      # Return the final counts for each battery health category
  return counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  #Check if the counts match the expected values
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
