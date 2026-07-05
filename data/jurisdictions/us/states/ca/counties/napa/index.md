---
type: Jurisdiction
title: "Napa County, CA"
classification: county
fips: "06055"
state: "CA"
demographics:
  population: 134869
  population_under_18: 26226
  population_18_64: 80188
  population_65_plus: 28455
  median_household_income: 111471
  poverty_rate: 8.46
  homeownership_rate: 63.41
  unemployment_rate: 5.2
  median_home_value: 869500
  gini_index: 0.4931
  vacancy_rate: 10.85
  race_white: 75020
  race_black: 2684
  race_asian: 11077
  race_native: 1546
  hispanic: 49046
  bachelors_plus: 52459
districts:
  - to: "us/states/ca/districts/04"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/ca/districts/senate/3"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ca/districts/house/4"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Napa County, CA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 134869 |
| Under 18 | 26226 |
| 18–64 | 80188 |
| 65+ | 28455 |
| Median household income | 111471 |
| Poverty rate | 8.46 |
| Homeownership rate | 63.41 |
| Unemployment rate | 5.2 |
| Median home value | 869500 |
| Gini index | 0.4931 |
| Vacancy rate | 10.85 |
| White | 75020 |
| Black | 2684 |
| Asian | 11077 |
| Native | 1546 |
| Hispanic/Latino | 49046 |
| Bachelor's or higher | 52459 |

## Districts

- [CA-04](/us/states/ca/districts/04.md) — 100% (congressional)
- [CA Senate District 3](/us/states/ca/districts/senate/3.md) — 100% (state senate)
- [CA House District 4](/us/states/ca/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
