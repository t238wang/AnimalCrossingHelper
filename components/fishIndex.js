import React, { Component } from 'react';
import { StyleSheet, Text, View, Dimensions, Image, TouchableOpacity, Button } from 'react-native';
import { FlatGrid } from 'react-native-super-grid';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { Fishes as fishData, FishPictures as fishPictures } from '../data/fishes';

export default class FishIndex extends Component {
  static navigationOptions = {
    headerTitle: '🐠鱼类图鉴',
    headerStyle: {
      height: 100,
      backgroundColor: '#bcc4f2',
    }
  }
  constructor(props) {
    super(props);
    this.state = {
      currentSelection: -1,
      hilightCurrentAvailableFish: false,
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

  isFishAvailNow = (months, hours) => {
    const curMonth = new Date().getMonth() + 1;
    const curHours = new Date().getHours();
    // hours is in the format of a-b, c-d
    if(!months.includes(curMonth)){
      return false;
    }
    if(hours === "一整天"){
      return true;
    }
    const hourSegments = hours.split(',');
    let isInRightHours = false;
    hourSegments.map((segment) => {
      const hours = segment.split('-');
      const start = hours[0];
      const end = hours[1];
      if(start > end) {
        // example, 17 - 9
        if(curHours > start || curHours < end) {
          isInRightHours = true;
        }
      } else {
        // example 9 to 17
        if (curHours > start && curHours < end) {
          isInRightHours = true;
        }
      }
    })
    return isInRightHours;
  }

  render(){
    const { currentSelection, hilightCurrentAvailableFish } = this.state;
    const { height } = Dimensions.get('window');
    const contentHeight = height * 0.6;
    const heightPerItem = contentHeight / 5;
    return (
        <View style={styles.pageWrapper}>
          <View style={styles.rowWrapper}>
            <MaterialCommunityIcons name="check-circle" size={20} color='#bcc4f2' />
            <Text style={{ marginRight: 8 }}>为现在可能出现的鱼</Text>
          </View>
          <FlatGrid
            itemDimension={heightPerItem}
            items={fishData}
            style={[styles.gridView]}
            staticDimension={contentHeight + 30}
            spacing={2}
            horizontal
            showsHorizontalScrollIndicator={false}
            renderItem={({ item, index }) => (
              <TouchableOpacity
                style={currentSelection === index ? styles.selectedItemContainer : styles.itemContainer}
                onPress={() => {
                  this.setState({currentSelection: index})
                }}
              >
                {this.isFishAvailNow(item.availMonths.north, item.time) ? <MaterialCommunityIcons name="check-circle" size={20} color='#bcc4f2' style={styles.availableMark}/> : null}
                <Image source={fishPictures(index)} style={{height: 80, width: 80, overflow: 'hidden'}} />
                <Text style={styles.itemName}>{item.name}</Text>
              </TouchableOpacity>
            )}
          />
          {currentSelection !== -1 ? <View style={styles.descriptionFlexBox}>
            <Text style={styles.descriptiveFullLineStrings}>{fishData[currentSelection].name}</Text>
            <Text style={styles.descriptiveStrings}>{`💰: ${fishData[currentSelection].price}`}</Text>
            <Text style={styles.descriptiveStrings}>{`📍: ${fishData[currentSelection].location}`}</Text>
            <Text style={styles.descriptiveStrings}>{`📐: ${fishData[currentSelection].shadowSize}`}</Text>
            <Text style={styles.descriptiveStrings}>{`⏰: ${fishData[currentSelection].time}`}</Text>
            <Text style={styles.descriptiveFullLineStrings}>{`🗓: ${this.getMonthsString()}`}</Text>
          </View>: null}
        </View>);
  }
}
const styles = StyleSheet.create({
  pageWrapper: {
    flex: 1,
    flexDirection: 'column',
    paddingHorizontal: 8,
    alignContent: "stretch",
    alignItems: "stretch",
    backgroundColor: '#F2EABC',
    paddingTop: 20,
  },
  rowWrapper:{
    flexDirection: "row",
    justifyContent: 'flex-end'
  },
  gridView: {
    marginVertical: 20,
    flexGrow: 0,
  },
  itemContainer: {
    padding: 3,
    flex: 1,
    borderWidth: 1.5,
    borderRadius: 10,
    borderColor: '#CCC'
  },
  selectedItemContainer: {
    padding: 3,
    flex: 1,
    borderWidth: 1.5,
    borderRadius: 10,
    borderColor: '#dd6b20'
  },
  itemName: {
    fontSize: 14,
    fontWeight: '600',
    textAlign: 'center',
  },
  titleText: {
    fontSize: 18,
  },
  descriptiveStrings: {
    fontWeight: '600',
    marginVertical: 2,
    width: '50%',
  },
  descriptiveFullLineStrings: {
    fontWeight: '600',
    marginVertical: 2,
    width: '100%',
  },
  availableMark: {
    position: "absolute",
    top: 0, 
    right: 0,
    zIndex: 1,
  },
  descriptionFlexBox: {
    flex: 1,
    flexDirection: 'row',
    flexWrap: 'wrap',
  }
});
