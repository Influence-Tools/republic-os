---
type: Jurisdiction
title: "Greene County, IL"
classification: county
fips: "17061"
state: "IL"
demographics:
  population: 11683
  population_under_18: 2575
  population_18_64: 6674
  population_65_plus: 2434
  median_household_income: 62192
  poverty_rate: 14.26
  homeownership_rate: 78.23
  unemployment_rate: 4.86
  median_home_value: 95200
  gini_index: 0.4457
  vacancy_rate: 23.04
  race_white: 11198
  race_black: 88
  race_asian: 61
  race_native: 16
  hispanic: 128
  bachelors_plus: 2069
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Greene County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11683 |
| Under 18 | 2575 |
| 18–64 | 6674 |
| 65+ | 2434 |
| Median household income | 62192 |
| Poverty rate | 14.26 |
| Homeownership rate | 78.23 |
| Unemployment rate | 4.86 |
| Median home value | 95200 |
| Gini index | 0.4457 |
| Vacancy rate | 23.04 |
| White | 11198 |
| Black | 88 |
| Asian | 61 |
| Native | 16 |
| Hispanic/Latino | 128 |
| Bachelor's or higher | 2069 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 100](/us/states/il/districts/house/100.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
