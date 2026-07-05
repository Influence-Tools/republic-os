---
type: Jurisdiction
title: "Evangeline Parish, LA"
classification: county
fips: "22039"
state: "LA"
demographics:
  population: 32060
  population_under_18: 8251
  population_18_64: 18667
  population_65_plus: 5142
  median_household_income: 41915
  poverty_rate: 24.26
  homeownership_rate: 66.24
  unemployment_rate: 9.81
  median_home_value: 124600
  gini_index: 0.4825
  vacancy_rate: 13.83
  race_white: 20895
  race_black: 8168
  race_asian: 125
  race_native: 43
  hispanic: 1586
  bachelors_plus: 3597
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/la/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/la/districts/house/38"
    rel: in-district
    area_weight: 0.8825
  - to: "us/states/la/districts/house/41"
    rel: in-district
    area_weight: 0.1173
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Evangeline Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 32060 |
| Under 18 | 8251 |
| 18–64 | 18667 |
| 65+ | 5142 |
| Median household income | 41915 |
| Poverty rate | 24.26 |
| Homeownership rate | 66.24 |
| Unemployment rate | 9.81 |
| Median home value | 124600 |
| Gini index | 0.4825 |
| Vacancy rate | 13.83 |
| White | 20895 |
| Black | 8168 |
| Asian | 125 |
| Native | 43 |
| Hispanic/Latino | 1586 |
| Bachelor's or higher | 3597 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 28](/us/states/la/districts/senate/28.md) — 100% (state senate)
- [LA House District 38](/us/states/la/districts/house/38.md) — 88% (state house)
- [LA House District 41](/us/states/la/districts/house/41.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
