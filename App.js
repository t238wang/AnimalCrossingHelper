import React, { Component } from 'react';
import { StyleSheet, Text, View, Dimensions, Image, TouchableOpacity } from 'react-native';
import MainStackNavigator from './components/mainNavigator';
import { NavigationContainer } from '@react-navigation/native';
import { createAppContainer } from 'react-navigation';

const AppContainer = createAppContainer(MainStackNavigator);

export default class App extends Component {
  render(){
    return <AppContainer />;
  }
}
