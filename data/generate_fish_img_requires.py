print("export const FishPictures = (idx) => {")
print("  switch(idx) {")
for x in range(0, 80):
    print('    case {0}:'.format(x))
    print("      return require('../assets/fishes/{0}.jpg');".format(x))
print('  }')
print('}')