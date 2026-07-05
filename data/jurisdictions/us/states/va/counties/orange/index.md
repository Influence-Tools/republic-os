---
type: Jurisdiction
title: "Orange County, VA"
classification: county
fips: "51137"
state: "VA"
demographics:
  population: 37822
  population_under_18: 8191
  population_18_64: 21930
  population_65_plus: 7701
  median_household_income: 94008
  poverty_rate: 9.83
  homeownership_rate: 78.68
  unemployment_rate: 3.36
  median_home_value: 364200
  gini_index: 0.4037
  vacancy_rate: 7.9
  race_white: 28900
  race_black: 3812
  race_asian: 378
  race_native: 12
  hispanic: 2650
  bachelors_plus: 10923
districts:
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/va/districts/senate/28"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/va/districts/house/62"
    rel: in-district
    area_weight: 0.5429
  - to: "us/states/va/districts/house/63"
    rel: in-district
    area_weight: 0.4569
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Orange County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37822 |
| Under 18 | 8191 |
| 18–64 | 21930 |
| 65+ | 7701 |
| Median household income | 94008 |
| Poverty rate | 9.83 |
| Homeownership rate | 78.68 |
| Unemployment rate | 3.36 |
| Median home value | 364200 |
| Gini index | 0.4037 |
| Vacancy rate | 7.9 |
| White | 28900 |
| Black | 3812 |
| Asian | 378 |
| Native | 12 |
| Hispanic/Latino | 2650 |
| Bachelor's or higher | 10923 |

## Districts

- [VA-07](/us/states/va/districts/07.md) — 100% (congressional)
- [VA Senate District 28](/us/states/va/districts/senate/28.md) — 100% (state senate)
- [VA House District 62](/us/states/va/districts/house/62.md) — 54% (state house)
- [VA House District 63](/us/states/va/districts/house/63.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
