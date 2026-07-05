---
type: Jurisdiction
title: "Chesterfield County, SC"
classification: county
fips: "45025"
state: "SC"
demographics:
  population: 43784
  population_under_18: 9709
  population_18_64: 25743
  population_65_plus: 8332
  median_household_income: 49235
  poverty_rate: 20.34
  homeownership_rate: 72.77
  unemployment_rate: 7.5
  median_home_value: 116200
  gini_index: 0.4836
  vacancy_rate: 15.88
  race_white: 26464
  race_black: 13165
  race_asian: 202
  race_native: 287
  hispanic: 2572
  bachelors_plus: 6047
districts:
  - to: "us/states/sc/districts/07"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/sc/districts/senate/27"
    rel: in-district
    area_weight: 0.8455
  - to: "us/states/sc/districts/senate/29"
    rel: in-district
    area_weight: 0.1544
  - to: "us/states/sc/districts/house/53"
    rel: in-district
    area_weight: 0.6515
  - to: "us/states/sc/districts/house/65"
    rel: in-district
    area_weight: 0.1941
  - to: "us/states/sc/districts/house/54"
    rel: in-district
    area_weight: 0.1544
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Chesterfield County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43784 |
| Under 18 | 9709 |
| 18–64 | 25743 |
| 65+ | 8332 |
| Median household income | 49235 |
| Poverty rate | 20.34 |
| Homeownership rate | 72.77 |
| Unemployment rate | 7.5 |
| Median home value | 116200 |
| Gini index | 0.4836 |
| Vacancy rate | 15.88 |
| White | 26464 |
| Black | 13165 |
| Asian | 202 |
| Native | 287 |
| Hispanic/Latino | 2572 |
| Bachelor's or higher | 6047 |

## Districts

- [SC-07](/us/states/sc/districts/07.md) — 100% (congressional)
- [SC Senate District 27](/us/states/sc/districts/senate/27.md) — 85% (state senate)
- [SC Senate District 29](/us/states/sc/districts/senate/29.md) — 15% (state senate)
- [SC House District 53](/us/states/sc/districts/house/53.md) — 65% (state house)
- [SC House District 65](/us/states/sc/districts/house/65.md) — 19% (state house)
- [SC House District 54](/us/states/sc/districts/house/54.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
