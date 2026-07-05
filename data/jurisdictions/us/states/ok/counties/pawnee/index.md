---
type: Jurisdiction
title: "Pawnee County, OK"
classification: county
fips: "40117"
state: "OK"
demographics:
  population: 15795
  population_under_18: 3665
  population_18_64: 8956
  population_65_plus: 3174
  median_household_income: 58738
  poverty_rate: 18.2
  homeownership_rate: 79.5
  unemployment_rate: 4.41
  median_home_value: 131500
  gini_index: 0.4425
  vacancy_rate: 16.63
  race_white: 12026
  race_black: 131
  race_asian: 81
  race_native: 1442
  hispanic: 615
  bachelors_plus: 2395
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/20"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/house/35"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Pawnee County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15795 |
| Under 18 | 3665 |
| 18–64 | 8956 |
| 65+ | 3174 |
| Median household income | 58738 |
| Poverty rate | 18.2 |
| Homeownership rate | 79.5 |
| Unemployment rate | 4.41 |
| Median home value | 131500 |
| Gini index | 0.4425 |
| Vacancy rate | 16.63 |
| White | 12026 |
| Black | 131 |
| Asian | 81 |
| Native | 1442 |
| Hispanic/Latino | 615 |
| Bachelor's or higher | 2395 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 20](/us/states/ok/districts/senate/20.md) — 100% (state senate)
- [OK House District 35](/us/states/ok/districts/house/35.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
