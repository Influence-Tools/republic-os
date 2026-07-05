---
type: Jurisdiction
title: "Anderson County, SC"
classification: county
fips: "45007"
state: "SC"
demographics:
  population: 210478
  population_under_18: 47554
  population_18_64: 124119
  population_65_plus: 38805
  median_household_income: 66651
  poverty_rate: 14.57
  homeownership_rate: 74.85
  unemployment_rate: 5.26
  median_home_value: 231900
  gini_index: 0.4668
  vacancy_rate: 9.12
  race_white: 161072
  race_black: 28586
  race_asian: 2221
  race_native: 1367
  hispanic: 10853
  bachelors_plus: 52481
districts:
  - to: "us/states/sc/districts/03"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/sc/districts/senate/4"
    rel: in-district
    area_weight: 0.5324
  - to: "us/states/sc/districts/senate/3"
    rel: in-district
    area_weight: 0.4672
  - to: "us/states/sc/districts/house/7"
    rel: in-district
    area_weight: 0.3169
  - to: "us/states/sc/districts/house/6"
    rel: in-district
    area_weight: 0.2043
  - to: "us/states/sc/districts/house/8"
    rel: in-district
    area_weight: 0.1829
  - to: "us/states/sc/districts/house/11"
    rel: in-district
    area_weight: 0.165
  - to: "us/states/sc/districts/house/9"
    rel: in-district
    area_weight: 0.068
  - to: "us/states/sc/districts/house/10"
    rel: in-district
    area_weight: 0.0627
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Anderson County, SC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 210478 |
| Under 18 | 47554 |
| 18–64 | 124119 |
| 65+ | 38805 |
| Median household income | 66651 |
| Poverty rate | 14.57 |
| Homeownership rate | 74.85 |
| Unemployment rate | 5.26 |
| Median home value | 231900 |
| Gini index | 0.4668 |
| Vacancy rate | 9.12 |
| White | 161072 |
| Black | 28586 |
| Asian | 2221 |
| Native | 1367 |
| Hispanic/Latino | 10853 |
| Bachelor's or higher | 52481 |

## Districts

- [SC-03](/us/states/sc/districts/03.md) — 100% (congressional)
- [SC Senate District 4](/us/states/sc/districts/senate/4.md) — 53% (state senate)
- [SC Senate District 3](/us/states/sc/districts/senate/3.md) — 47% (state senate)
- [SC House District 7](/us/states/sc/districts/house/7.md) — 32% (state house)
- [SC House District 6](/us/states/sc/districts/house/6.md) — 20% (state house)
- [SC House District 8](/us/states/sc/districts/house/8.md) — 18% (state house)
- [SC House District 11](/us/states/sc/districts/house/11.md) — 16% (state house)
- [SC House District 9](/us/states/sc/districts/house/9.md) — 7% (state house)
- [SC House District 10](/us/states/sc/districts/house/10.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
