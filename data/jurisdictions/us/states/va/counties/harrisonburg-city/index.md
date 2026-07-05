---
type: Jurisdiction
title: "Harrisonburg city, VA"
classification: county
fips: "51660"
state: "VA"
demographics:
  population: 51392
  population_under_18: 15547
  population_18_64: 21926
  population_65_plus: 13919
  median_household_income: 62254
  poverty_rate: 25.71
  homeownership_rate: 39.49
  unemployment_rate: 6.86
  median_home_value: 299100
  gini_index: 0.4543
  vacancy_rate: 7.0
  race_white: 33036
  race_black: 3938
  race_asian: 1837
  race_native: 271
  hispanic: 12119
  bachelors_plus: 14450
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/2"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/34"
    rel: in-district
    area_weight: 0.9989
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Harrisonburg city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51392 |
| Under 18 | 15547 |
| 18–64 | 21926 |
| 65+ | 13919 |
| Median household income | 62254 |
| Poverty rate | 25.71 |
| Homeownership rate | 39.49 |
| Unemployment rate | 6.86 |
| Median home value | 299100 |
| Gini index | 0.4543 |
| Vacancy rate | 7.0 |
| White | 33036 |
| Black | 3938 |
| Asian | 1837 |
| Native | 271 |
| Hispanic/Latino | 12119 |
| Bachelor's or higher | 14450 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 100% (congressional)
- [VA Senate District 2](/us/states/va/districts/senate/2.md) — 100% (state senate)
- [VA House District 34](/us/states/va/districts/house/34.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
