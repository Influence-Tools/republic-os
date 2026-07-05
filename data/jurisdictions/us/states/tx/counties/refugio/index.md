---
type: Jurisdiction
title: "Refugio County, TX"
classification: county
fips: "48391"
state: "TX"
demographics:
  population: 6707
  population_under_18: 1457
  population_18_64: 3739
  population_65_plus: 1511
  median_household_income: 60181
  poverty_rate: 14.63
  homeownership_rate: 76.99
  unemployment_rate: 4.51
  median_home_value: 99000
  gini_index: 0.4266
  vacancy_rate: 25.72
  race_white: 3799
  race_black: 480
  race_asian: 0
  race_native: 19
  hispanic: 3382
  bachelors_plus: 819
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9768
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9596
  - to: "us/states/tx/districts/house/43"
    rel: in-district
    area_weight: 0.9594
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Refugio County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6707 |
| Under 18 | 1457 |
| 18–64 | 3739 |
| 65+ | 1511 |
| Median household income | 60181 |
| Poverty rate | 14.63 |
| Homeownership rate | 76.99 |
| Unemployment rate | 4.51 |
| Median home value | 99000 |
| Gini index | 0.4266 |
| Vacancy rate | 25.72 |
| White | 3799 |
| Black | 480 |
| Asian | 0 |
| Native | 19 |
| Hispanic/Latino | 3382 |
| Bachelor's or higher | 819 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 98% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 96% (state senate)
- [TX House District 43](/us/states/tx/districts/house/43.md) — 96% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
