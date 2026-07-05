---
type: Jurisdiction
title: "Perry County, IL"
classification: county
fips: "17145"
state: "IL"
demographics:
  population: 20639
  population_under_18: 3979
  population_18_64: 12475
  population_65_plus: 4185
  median_household_income: 62118
  poverty_rate: 16.94
  homeownership_rate: 80.94
  unemployment_rate: 4.56
  median_home_value: 112600
  gini_index: 0.4125
  vacancy_rate: 13.95
  race_white: 17644
  race_black: 1573
  race_asian: 74
  race_native: 10
  hispanic: 760
  bachelors_plus: 2706
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/115"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Perry County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20639 |
| Under 18 | 3979 |
| 18–64 | 12475 |
| 65+ | 4185 |
| Median household income | 62118 |
| Poverty rate | 16.94 |
| Homeownership rate | 80.94 |
| Unemployment rate | 4.56 |
| Median home value | 112600 |
| Gini index | 0.4125 |
| Vacancy rate | 13.95 |
| White | 17644 |
| Black | 1573 |
| Asian | 74 |
| Native | 10 |
| Hispanic/Latino | 760 |
| Bachelor's or higher | 2706 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 100% (state senate)
- [IL House District 115](/us/states/il/districts/house/115.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
