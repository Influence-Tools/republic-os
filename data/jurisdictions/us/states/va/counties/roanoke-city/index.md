---
type: Jurisdiction
title: "Roanoke city, VA"
classification: county
fips: "51770"
state: "VA"
demographics:
  population: 98355
  population_under_18: 24168
  population_18_64: 32938
  population_65_plus: 41249
  median_household_income: 55378
  poverty_rate: 18.33
  homeownership_rate: 52.44
  unemployment_rate: 5.61
  median_home_value: 190500
  gini_index: 0.5082
  vacancy_rate: 11.26
  race_white: 55840
  race_black: 27466
  race_asian: 3082
  race_native: 136
  hispanic: 8823
  bachelors_plus: 28585
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.9959
  - to: "us/states/va/districts/senate/4"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/va/districts/house/38"
    rel: in-district
    area_weight: 0.8674
  - to: "us/states/va/districts/house/40"
    rel: in-district
    area_weight: 0.1317
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Roanoke city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98355 |
| Under 18 | 24168 |
| 18–64 | 32938 |
| 65+ | 41249 |
| Median household income | 55378 |
| Poverty rate | 18.33 |
| Homeownership rate | 52.44 |
| Unemployment rate | 5.61 |
| Median home value | 190500 |
| Gini index | 0.5082 |
| Vacancy rate | 11.26 |
| White | 55840 |
| Black | 27466 |
| Asian | 3082 |
| Native | 136 |
| Hispanic/Latino | 8823 |
| Bachelor's or higher | 28585 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 4](/us/states/va/districts/senate/4.md) — 100% (state senate)
- [VA House District 38](/us/states/va/districts/house/38.md) — 87% (state house)
- [VA House District 40](/us/states/va/districts/house/40.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
