---
type: Jurisdiction
title: "Union County, NM"
classification: county
fips: "35059"
state: "NM"
demographics:
  population: 4013
  population_under_18: 856
  population_18_64: 2241
  population_65_plus: 916
  median_household_income: 46694
  poverty_rate: 16.58
  homeownership_rate: 72.39
  unemployment_rate: 6.18
  median_home_value: 122700
  gini_index: 0.649
  vacancy_rate: 31.56
  race_white: 2559
  race_black: 43
  race_asian: 0
  race_native: 145
  hispanic: 1609
  bachelors_plus: 696
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nm/districts/senate/7"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nm/districts/house/67"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Union County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4013 |
| Under 18 | 856 |
| 18–64 | 2241 |
| 65+ | 916 |
| Median household income | 46694 |
| Poverty rate | 16.58 |
| Homeownership rate | 72.39 |
| Unemployment rate | 6.18 |
| Median home value | 122700 |
| Gini index | 0.649 |
| Vacancy rate | 31.56 |
| White | 2559 |
| Black | 43 |
| Asian | 0 |
| Native | 145 |
| Hispanic/Latino | 1609 |
| Bachelor's or higher | 696 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 7](/us/states/nm/districts/senate/7.md) — 100% (state senate)
- [NM House District 67](/us/states/nm/districts/house/67.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
