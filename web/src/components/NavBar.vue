<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <router-link class="navbar-brand" :to="{name: 'home'}">VICTORY</router-link>
              <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <router-link :class="route_name == 'function1_index' ? 'nav-link active' : 'nav-link'" :to="{name: 'function1_index'}">功能一</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link :class="route_name == 'function2_index' ? 'nav-link active' : 'nav-link'" :to="{name: 'function2_index'}">功能二</router-link>
                  </li>
                  <li class="nav-item">
                    <router-link :class="route_name == 'function3_index' ? 'nav-link active' : 'nav-link'" :to="{name: 'function3_index'}">功能三</router-link>
                  </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          用户名
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                          <li>
                            <router-link class="dropdown-item" :to="{name: 'user_bot_index'}">我的订阅</router-link>
                          </li>
                          <li><hr class="dropdown-divider"></li>
                          <li><a class="dropdown-item" href="#">退出</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>  
</template>
    
    <script>
    import { useRoute } from 'vue-router'
    import { computed } from 'vue'
    
    export default {
        setup() {
            const route = useRoute();
            let route_name = computed(() => route.name)
            return {
                route_name
            }
        }
    }
    </script>
    
    <style scoped>
    
    </style>  
    
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>