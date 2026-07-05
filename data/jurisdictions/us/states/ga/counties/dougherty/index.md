---
type: Jurisdiction
title: "Dougherty County, GA"
classification: county
fips: "13095"
state: "GA"
demographics:
  population: 83091
  population_under_18: 20025
  population_18_64: 48623
  population_65_plus: 14443
  median_household_income: 49044
  poverty_rate: 25.03
  homeownership_rate: 45.33
  unemployment_rate: 10.2
  median_home_value: 134400
  gini_index: 0.4759
  vacancy_rate: 15.68
  race_white: 19277
  race_black: 58613
  race_asian: 592
  race_native: 178
  hispanic: 2710
  bachelors_plus: 18479
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9967
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.3622
  - to: "us/states/ga/districts/house/151"
    rel: in-district
    area_weight: 0.2244
  - to: "us/states/ga/districts/house/152"
    rel: in-district
    area_weight: 0.207
  - to: "us/states/ga/districts/house/153"
    rel: in-district
    area_weight: 0.2064
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Dougherty County, GA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 83091 |
| Under 18 | 20025 |
| 18–64 | 48623 |
| 65+ | 14443 |
| Median household income | 49044 |
| Poverty rate | 25.03 |
| Homeownership rate | 45.33 |
| Unemployment rate | 10.2 |
| Median home value | 134400 |
| Gini index | 0.4759 |
| Vacancy rate | 15.68 |
| White | 19277 |
| Black | 58613 |
| Asian | 592 |
| Native | 178 |
| Hispanic/Latino | 2710 |
| Bachelor's or higher | 18479 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 100% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 36% (state house)
- [GA House District 151](/us/states/ga/districts/house/151.md) — 22% (state house)
- [GA House District 152](/us/states/ga/districts/house/152.md) — 21% (state house)
- [GA House District 153](/us/states/ga/districts/house/153.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
