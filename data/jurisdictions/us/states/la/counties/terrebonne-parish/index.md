---
type: Jurisdiction
title: "Terrebonne Parish, LA"
classification: county
fips: "22109"
state: "LA"
demographics:
  population: 106186
  population_under_18: 26565
  population_18_64: 62800
  population_65_plus: 16821
  median_household_income: 64836
  poverty_rate: 16.01
  homeownership_rate: 75.33
  unemployment_rate: 4.68
  median_home_value: 187200
  gini_index: 0.465
  vacancy_rate: 11.11
  race_white: 68490
  race_black: 19664
  race_asian: 1161
  race_native: 5340
  hispanic: 7696
  bachelors_plus: 17845
districts:
  - to: "us/states/la/districts/03"
    rel: in-district
    area_weight: 0.727
  - to: "us/states/la/districts/senate/20"
    rel: in-district
    area_weight: 0.5254
  - to: "us/states/la/districts/senate/21"
    rel: in-district
    area_weight: 0.1886
  - to: "us/states/la/districts/house/53"
    rel: in-district
    area_weight: 0.4911
  - to: "us/states/la/districts/house/51"
    rel: in-district
    area_weight: 0.1897
  - to: "us/states/la/districts/house/52"
    rel: in-district
    area_weight: 0.0331
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Terrebonne Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 106186 |
| Under 18 | 26565 |
| 18–64 | 62800 |
| 65+ | 16821 |
| Median household income | 64836 |
| Poverty rate | 16.01 |
| Homeownership rate | 75.33 |
| Unemployment rate | 4.68 |
| Median home value | 187200 |
| Gini index | 0.465 |
| Vacancy rate | 11.11 |
| White | 68490 |
| Black | 19664 |
| Asian | 1161 |
| Native | 5340 |
| Hispanic/Latino | 7696 |
| Bachelor's or higher | 17845 |

## Districts

- [LA-03](/us/states/la/districts/03.md) — 73% (congressional)
- [LA Senate District 20](/us/states/la/districts/senate/20.md) — 53% (state senate)
- [LA Senate District 21](/us/states/la/districts/senate/21.md) — 19% (state senate)
- [LA House District 53](/us/states/la/districts/house/53.md) — 49% (state house)
- [LA House District 51](/us/states/la/districts/house/51.md) — 19% (state house)
- [LA House District 52](/us/states/la/districts/house/52.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
