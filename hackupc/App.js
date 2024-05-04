import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';


//Pantallas
import Pruebas from './screens/Pruebas';
import Home from './screens/Home';
import TravelPlan from './screens/TravelPlan';
import LoginScreen from './screens/LoginScreen';
import ActivityDetails from './screens/ActivityDetails';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={Home} options={{headerShown: true}} />
        <Stack.Screen name="TravelPlan" component={TravelPlan} options={{headerShown: true}}/>
        <Stack.Screen name="ActivityDetails" component={ActivityDetails} options={{headerShown: true}}/>
        <Stack.Screen name="Pruebas" component={Pruebas} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
