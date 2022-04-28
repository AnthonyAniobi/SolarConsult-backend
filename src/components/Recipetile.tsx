import React from 'react';
import './style.css';

function Recipetile({ recipe }: { recipe: any }) {
  const rExp: RegExp = /\.(png|jpg|gif|jpeg)$/;
  const imgUrl: string = recipe.recipe.image as string;
  return (

    <div className='recipeTile' onClick={(e) => window.open(recipe.recipe.url)}>
      <img className='recipeTile__image' src={recipe.recipe.image} alt={` image of ${recipe.recipe.label}`} />
      <p className='recipeTile__name'>{recipe.recipe.label}</p>

    </div>
  )
}

export default Recipetile