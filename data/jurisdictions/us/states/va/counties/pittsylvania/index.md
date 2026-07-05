---
type: Jurisdiction
title: "Pittsylvania County, VA"
classification: county
fips: "51143"
state: "VA"
demographics:
  population: 59856
  population_under_18: 10718
  population_18_64: 34465
  population_65_plus: 14673
  median_household_income: 54085
  poverty_rate: 14.56
  homeownership_rate: 78.67
  unemployment_rate: 4.68
  median_home_value: 161400
  gini_index: 0.4386
  vacancy_rate: 15.02
  race_white: 44353
  race_black: 12175
  race_asian: 185
  race_native: 33
  hispanic: 1857
  bachelors_plus: 9385
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.999
  - to: "us/states/va/districts/senate/9"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/48"
    rel: in-district
    area_weight: 0.774
  - to: "us/states/va/districts/house/49"
    rel: in-district
    area_weight: 0.1927
  - to: "us/states/va/districts/house/51"
    rel: in-district
    area_weight: 0.0332
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Pittsylvania County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59856 |
| Under 18 | 10718 |
| 18–64 | 34465 |
| 65+ | 14673 |
| Median household income | 54085 |
| Poverty rate | 14.56 |
| Homeownership rate | 78.67 |
| Unemployment rate | 4.68 |
| Median home value | 161400 |
| Gini index | 0.4386 |
| Vacancy rate | 15.02 |
| White | 44353 |
| Black | 12175 |
| Asian | 185 |
| Native | 33 |
| Hispanic/Latino | 1857 |
| Bachelor's or higher | 9385 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 9](/us/states/va/districts/senate/9.md) — 100% (state senate)
- [VA House District 48](/us/states/va/districts/house/48.md) — 77% (state house)
- [VA House District 49](/us/states/va/districts/house/49.md) — 19% (state house)
- [VA House District 51](/us/states/va/districts/house/51.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
