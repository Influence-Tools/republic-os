---
type: Jurisdiction
title: "Grundy County, IL"
classification: county
fips: "17063"
state: "IL"
demographics:
  population: 53219
  population_under_18: 12939
  population_18_64: 32249
  population_65_plus: 8031
  median_household_income: 92235
  poverty_rate: 5.99
  homeownership_rate: 74.38
  unemployment_rate: 4.58
  median_home_value: 271700
  gini_index: 0.4036
  vacancy_rate: 3.69
  race_white: 45933
  race_black: 1220
  race_asian: 301
  race_native: 38
  hispanic: 6368
  bachelors_plus: 11067
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.7101
  - to: "us/states/il/districts/senate/38"
    rel: in-district
    area_weight: 0.2485
  - to: "us/states/il/districts/senate/40"
    rel: in-district
    area_weight: 0.0414
  - to: "us/states/il/districts/house/106"
    rel: in-district
    area_weight: 0.7101
  - to: "us/states/il/districts/house/75"
    rel: in-district
    area_weight: 0.2485
  - to: "us/states/il/districts/house/79"
    rel: in-district
    area_weight: 0.0414
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Grundy County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 53219 |
| Under 18 | 12939 |
| 18–64 | 32249 |
| 65+ | 8031 |
| Median household income | 92235 |
| Poverty rate | 5.99 |
| Homeownership rate | 74.38 |
| Unemployment rate | 4.58 |
| Median home value | 271700 |
| Gini index | 0.4036 |
| Vacancy rate | 3.69 |
| White | 45933 |
| Black | 1220 |
| Asian | 301 |
| Native | 38 |
| Hispanic/Latino | 6368 |
| Bachelor's or higher | 11067 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 71% (state senate)
- [IL Senate District 38](/us/states/il/districts/senate/38.md) — 25% (state senate)
- [IL Senate District 40](/us/states/il/districts/senate/40.md) — 4% (state senate)
- [IL House District 106](/us/states/il/districts/house/106.md) — 71% (state house)
- [IL House District 75](/us/states/il/districts/house/75.md) — 25% (state house)
- [IL House District 79](/us/states/il/districts/house/79.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
