---
type: Jurisdiction
title: "Adams County, IL"
classification: county
fips: "17001"
state: "IL"
demographics:
  population: 64754
  population_under_18: 14578
  population_18_64: 36859
  population_65_plus: 13317
  median_household_income: 66220
  poverty_rate: 12.84
  homeownership_rate: 72.14
  unemployment_rate: 3.88
  median_home_value: 162600
  gini_index: 0.4535
  vacancy_rate: 7.88
  race_white: 58671
  race_black: 1839
  race_asian: 435
  race_native: 79
  hispanic: 1350
  bachelors_plus: 16343
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.7846
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.2153
  - to: "us/states/il/districts/house/99"
    rel: in-district
    area_weight: 0.4839
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.3008
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.2153
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Adams County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64754 |
| Under 18 | 14578 |
| 18–64 | 36859 |
| 65+ | 13317 |
| Median household income | 66220 |
| Poverty rate | 12.84 |
| Homeownership rate | 72.14 |
| Unemployment rate | 3.88 |
| Median home value | 162600 |
| Gini index | 0.4535 |
| Vacancy rate | 7.88 |
| White | 58671 |
| Black | 1839 |
| Asian | 435 |
| Native | 79 |
| Hispanic/Latino | 1350 |
| Bachelor's or higher | 16343 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 78% (state senate)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 22% (state senate)
- [IL House District 99](/us/states/il/districts/house/99.md) — 48% (state house)
- [IL House District 100](/us/states/il/districts/house/100.md) — 30% (state house)
- [IL House District 94](/us/states/il/districts/house/94.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
