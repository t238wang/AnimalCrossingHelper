import * as React from 'react';
import { createStackNavigator } from 'react-navigation-stack';
import Home from './home';
import FishIndex from './fishIndex';

const MainStackNavigator = createStackNavigator({
    'HOME_ROUTE': Home,
    'FISH_INDEX_ROUTE': FishIndex,
}, {
    initialRouteName: 'FISH_INDEX_ROUTE'
});

export default MainStackNavigator;