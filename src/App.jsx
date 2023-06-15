import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages/Home';
import StocksByIndustry from './pages/StockByIndustry';
import NewsByTicker from './pages/NewsByTicker';
import NewsByIndustry from './pages/NewsByIndustry';
import NewsBySource from './pages/NewsBySource';
import Admin from './pages/Admin';
import News from './pages/News';
import Industries from './pages/Industries';


const App = () => {
  return (
    <Router>
      <div className="flex flex-col items-center justify-center">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/stocks-by-industry" component={StocksByIndustry} />
          <Route path="/news-by-ticker" component={NewsByTicker} />
          <Route path="/news-by-industry" component={NewsByIndustry} />
          <Route path="/news-by-source" component={NewsBySource} />
          <Route path="/admin" component={Admin} />
          <Route path="/industries" component={Industries} />
          <Route path="/news" component={News} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
