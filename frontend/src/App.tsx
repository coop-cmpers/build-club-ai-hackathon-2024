import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
// import logo from './logo.svg';
import './App.css';
import Search from "./pages/search";
import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";

const theme = createTheme({
  palette: {
    background: {
      default: "#f9f1ea"
    }
  }
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Search />}/>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
