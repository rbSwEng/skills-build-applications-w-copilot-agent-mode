
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, NavLink } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
        <div className="container-fluid">
          <NavLink className="navbar-brand" to="/">
            <img src="/octofitapp-small.png" alt="Octofit Logo" className="navbar-brand-logo" />
            Octofit Tracker
          </NavLink>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink to="/activities" className={({ isActive }) => 'nav-link' + (isActive ? ' active' : '')}>Activities</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/leaderboard" className={({ isActive }) => 'nav-link' + (isActive ? ' active' : '')}>Leaderboard</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/teams" className={({ isActive }) => 'nav-link' + (isActive ? ' active' : '')}>Teams</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/users" className={({ isActive }) => 'nav-link' + (isActive ? ' active' : '')}>Users</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/workouts" className={({ isActive }) => 'nav-link' + (isActive ? ' active' : '')}>Workouts</NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={<Activities />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
