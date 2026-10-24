/**
 * Tokyo Snow Theme Demo File
 * This file showcases the theme's colours against the alley-wall background
 */

// Comments are in shadowed-pavement dim with italic styling

import axios from 'axios'; // Strings in moss green
import { useEffect, useState } from 'react'; // Keywords in neon red
import * as THREE from 'three'; // Variables in gold

const API_URL = 'https://api.example.com/data'; // Constants in ember
const MAX_RETRIES = 3; // Numbers in ember
const DEFAULT_TIMEOUT = 5000; // More numbers

// Class definition with types in amber
class DataProcessor {
  constructor(config) {
    this.apiUrl = API_URL; // `this` in italic neon, properties in sage
    this.retries = MAX_RETRIES;
    this.timeout = DEFAULT_TIMEOUT;
    this.isActive = true; // Boolean constants in ember
  }

  // Function names in pine green
  async fetchData(endpoint, options = {}) {
    try {
      const response = await axios.get(`${this.apiUrl}/${endpoint}`, {
        timeout: this.timeout,
        ...options
      });

      return response.data;
    } catch (error) {
      console.error('Failed to fetch data:', error.message);
      throw new Error(`API Error: ${error.status}`);
    }
  }

  // Method with various syntax elements showcasing bracket colors
  processResults(data, filters) {
    const results = data
      .filter(item => item.active && item.score > 0.8) // Operators in gold
      .map((item, index) => ({
        id: item.id || `generated-${index}`,
        title: item.title?.trim() || 'Untitled',
        score: Math.round(item.score * 100) / 100,
        tags: item.tags || [],
        createdAt: new Date(item.timestamp)
      }))
      .sort((a, b) => b.score - a.score);

    return results;
  }
}

// React component showing JSX highlighting
function ThemeDemo({ data, onUpdate }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (data?.length > 0) {
      console.log(`Processing ${data.length} items`);
    }
  }, [data]);

  return (
    <div className="theme-demo">
      <h1 style={{ color: '#e1b568' }}>Tokyo Snow Demo</h1>
      <p className="description">
        Vending-machine light on a snowy alley at night
      </p>

      {loading ? (
        <div className="spinner">Loading...</div>
      ) : error ? (
        <div className="error">Error: {error}</div>
      ) : (
        <ul>
          {data?.map(item => (
            <li key={item.id} onClick={() => onUpdate(item)}>
              {item.title}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// CSS-in-JS using the palette itself
const styles = {
  container: {
    backgroundColor: '#2a2a28', // shadow: the editor background
    color: '#ecd08f', // gold: body text
    padding: '20px',
    borderRadius: '8px'
  },
  button: {
    background: 'linear-gradient(45deg, #d5583d, #e1b568)', // neon to amber
    border: 'none',
    color: '#1c1c1a', // night
    fontSize: '16px'
  }
};

// Regular expressions in sage, template literals in moss
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const phonePattern = /^\d{3}-\d{3}-\d{4}$/;

function validateInput(email, phone) {
  const emailValid = EMAIL_REGEX.test(email);
  const phoneValid = phonePattern.test(phone);

  return {
    email: emailValid,
    phone: phoneValid,
    message: `Validation ${emailValid && phoneValid ? 'passed' : 'failed'}`
  };
}

// Async/await with error handling
async function initializeApp() {
  try {
    const processor = new DataProcessor({
      apiUrl: API_URL,
      timeout: 10000
    });

    const userData = await processor.fetchData('users');
    const processedData = processor.processResults(userData, {
      minScore: 0.5,
      activeOnly: true
    });

    console.log('App initialized successfully');
    return processedData;
  } catch (err) {
    console.error('Initialization failed:', err);
    return [];
  }
}

// Export statement with italic neon keywords
export { DataProcessor, initializeApp, ThemeDemo, validateInput };
export default ThemeDemo;
