import React, { useState, useEffect } from 'react';
import './App.css';
import Axios from 'axios';
import Recipetile from './components/Recipetile';

function App() {


  const healthOptions: Array<string> = ['vegetarian', 'alcohol-free',
    'immuno-supportive', 'celery-free', 'crustacean-free',
    'diary-free', 'egg-free', 'fish-free', 'fodmap-free',
    'gluten-free', 'keto-friendly', 'kidney-friendly',
    'kosher', 'low-potassium', 'lupine-free',
    'mustard-free', 'low-fat-abs', 'No-oil-added',
    'low-sugar', 'paleo', 'peanut-free',
    'pecatarian', 'pork-free', 'vegan'
  ];

  const [query, setQuery] = useState("");
  const [healthLabel, setHealthLabel] = useState(healthOptions[0]);
  const [recipes, setRecipes] = useState([]);

  let YOUR_APP_KEY: string = process.env.REACT_APP_APP_KEY as string;
  let YOUR_APP_ID: string = process.env.REACT_APP_APP_ID as string;
  const url: string = `https://api.edamam.com/search?q=${query}&app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}&health=${healthLabel}`;


  const getRecipeInfo = async () => {
    var result = await Axios.get(url);
    setRecipes(result.data.hits)
    console.log(result.data.hits)
  }

  const onSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    getRecipeInfo();
  }

  return (
    <div className="app">
      <h1 ><u>Intercontinental Food Recipes</u>🍔</h1>
      <form onSubmit={onSubmit} className="app__searchForm">
        <input type="text"
          placeholder='Type ingredient'
          autoComplete='Off'
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="app__input" />
        <select id="" className="app__healthLabels">
          {healthOptions.map((value: string) => {
            return <option key={value} value={value} onClick={(e) => setHealthLabel(value)}>{value}</option>
          })}

        </select>
        <input type="submit" value="Get Recipe" className="app__submit" />
      </form>
      <div className='recipeList'>
        {recipes.map((recipe: any) => {
          return <Recipetile key={recipe.recipe.label} recipe={recipe} />
        })}
      </div>
    </div>
  );
}

export default App;
