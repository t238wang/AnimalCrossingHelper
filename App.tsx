import React, { Component } from 'react';
import { StyleSheet, Text, View, Dimensions, Image, TouchableOpacity } from 'react-native';
import { FlatGrid } from 'react-native-super-grid';
import { Fishes as fishData, FishPictures as fishPictures } from './data/fishes';

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentSelection: -1,
    }
  }

  onItemPressed = (idx) => {
    this.setState({currentSelection: idx})
  }

  getMonthsString = () => {
    const { currentSelection } = this.state;
    if(currentSelection !== -1){
      return fishData[currentSelection].availMonths.north.map((month) => `${month}月`).join(',');
    }
  }

  render(){
    const { currentSelection } = this.state;
    const { height } = Dimensions.get('window');
    const contentHeight = height * 0.6;
    const heightPerItem = contentHeight / 5;
    return (
        <View style={styles.pageWrapper}>
          <View style={styles.descriptiveStrings}><Text>动物之森钓鱼图鉴🎣</Text></View>
          <View><Text>🌏: ⬆️</Text></View>
          <FlatGrid
            itemDimension={heightPerItem}
            items={fishData}
            style={[styles.gridView]}
            staticDimension={contentHeight + 30}
            spacing={5}
            horizontal
            showsHorizontalScrollIndicator={false}
            renderItem={({ item, index }) => (
              <TouchableOpacity
                style={currentSelection === index ? styles.selectedItemContainer : styles.itemContainer}
                onPress={() => {
                  this.setState({currentSelection: index})
                }}
              >
                <Image source={fishPictures(index)} style={{height: 80, width: 80}} />
                <Text style={styles.itemName}>{item.name}</Text>
              </TouchableOpacity>
            )}
          />
          {currentSelection !== -1 ? <View style={{marginBottom: 20}}>
            <Text style={styles.descriptiveStrings}>{fishData[currentSelection].name}</Text>
            <Text style={styles.descriptiveStrings}>{`💰: ${fishData[currentSelection].price}`}</Text>
            <Text style={styles.descriptiveStrings}>{`📍: ${fishData[currentSelection].location}`}</Text>
            <Text style={styles.descriptiveStrings}>{`📐: ${fishData[currentSelection].shadowSize}`}</Text>
            <Text style={styles.descriptiveStrings}>{`⏰: ${fishData[currentSelection].time}`}</Text>
            <Text style={styles.descriptiveStrings}>{`🗓: ${this.getMonthsString()}`}</Text>
          </View>: null}
        </View>);
  }
}
const styles = StyleSheet.create({
  pageWrapper: {
    flex: 1,
    marginTop: 50,
    flexDirection: 'column',
    paddingHorizontal: 8,
    alignContent: "stretch",
    alignItems: "stretch",
  },
  rowWrapper:{
    flexDirection: "row",
  },
  gridView: {
    marginVertical: 20,
  },
  itemContainer: {
    borderWidth: 1,
    borderRadius: 5,
    borderColor: '#CCC'
  },
  selectedItemContainer: {
    borderWidth: 1,
    borderRadius: 5,
    borderColor: '#dd6b20'
  },
  itemName: {
    fontSize: 14,
    fontWeight: '600',
    textAlign: 'center',
  },
  descriptiveStrings: {
    fontWeight: '600',
    marginVertical: 2,
  },
});
