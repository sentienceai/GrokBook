import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Library from './pages/Library';
import Settings from './pages/Settings';

const AppRoutes = () => (
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/library" element={<Library />} />
    <Route path="/settings" element={<Settings />} />
  </Routes>
);

export default AppRoutes;