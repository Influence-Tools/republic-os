---
type: Jurisdiction
title: "Waynesboro city, VA"
classification: county
fips: "51820"
state: "VA"
demographics:
  population: 22841
  population_under_18: 5107
  population_18_64: 13653
  population_65_plus: 4081
  median_household_income: 59994
  poverty_rate: 11.22
  homeownership_rate: 59.93
  unemployment_rate: 5.09
  median_home_value: 245500
  gini_index: 0.4195
  vacancy_rate: 6.37
  race_white: 16910
  race_black: 2711
  race_asian: 436
  race_native: 22
  hispanic: 2218
  bachelors_plus: 5697
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/va/districts/house/36"
    rel: in-district
    area_weight: 0.9982
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Waynesboro city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22841 |
| Under 18 | 5107 |
| 18–64 | 13653 |
| 65+ | 4081 |
| Median household income | 59994 |
| Poverty rate | 11.22 |
| Homeownership rate | 59.93 |
| Unemployment rate | 5.09 |
| Median home value | 245500 |
| Gini index | 0.4195 |
| Vacancy rate | 6.37 |
| White | 16910 |
| Black | 2711 |
| Asian | 436 |
| Native | 22 |
| Hispanic/Latino | 2218 |
| Bachelor's or higher | 5697 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 100% (state senate)
- [VA House District 36](/us/states/va/districts/house/36.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
