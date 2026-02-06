import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { isAuthenticated } from '../api/auth';

export const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();
  const location = useLocation();

  // Check both context user and localStorage token
  const hasValidAuth = user || isAuthenticated();

  if (loading && !hasValidAuth) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      </div>
    );
  }

  if (!hasValidAuth) {
    return <Navigate to="/login" state={{ from: location.pathname }} replace />;
  }

  return children;
};

export const AdminRoute = ({ children }) => {
  const { user, loading, isAdmin } = useAuth();
  const location = useLocation();

  // Check both context and localStorage
  const hasValidAuth = user || isAuthenticated();
  
  // Check if user is admin from token
  const checkIsAdmin = () => {
    if (isAdmin) return true;
    const token = localStorage.getItem('access_token');
    if (!token) return false;
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      return payload.role === 'admin';
    } catch {
      return false;
    }
  };

  if (loading && !hasValidAuth) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      </div>
    );
  }

  if (!hasValidAuth) {
    return <Navigate to="/admin/login" state={{ from: location.pathname }} replace />;
  }

  if (!checkIsAdmin()) {
    return <Navigate to="/" replace />;
  }

  return children;
};
