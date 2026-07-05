---
type: Jurisdiction
title: "Kendall County, IL"
classification: county
fips: "17093"
state: "IL"
demographics:
  population: 137675
  population_under_18: 37238
  population_18_64: 84971
  population_65_plus: 15466
  median_household_income: 111601
  poverty_rate: 5.42
  homeownership_rate: 84.03
  unemployment_rate: 4.34
  median_home_value: 322400
  gini_index: 0.3615
  vacancy_rate: 2.61
  race_white: 89865
  race_black: 10573
  race_asian: 4997
  race_native: 929
  hispanic: 30872
  bachelors_plus: 43982
districts:
  - to: "us/states/il/districts/14"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/il/districts/senate/38"
    rel: in-district
    area_weight: 0.8609
  - to: "us/states/il/districts/senate/42"
    rel: in-district
    area_weight: 0.0756
  - to: "us/states/il/districts/senate/49"
    rel: in-district
    area_weight: 0.0635
  - to: "us/states/il/districts/house/75"
    rel: in-district
    area_weight: 0.8609
  - to: "us/states/il/districts/house/97"
    rel: in-district
    area_weight: 0.0635
  - to: "us/states/il/districts/house/83"
    rel: in-district
    area_weight: 0.0507
  - to: "us/states/il/districts/house/84"
    rel: in-district
    area_weight: 0.0249
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Kendall County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 137675 |
| Under 18 | 37238 |
| 18–64 | 84971 |
| 65+ | 15466 |
| Median household income | 111601 |
| Poverty rate | 5.42 |
| Homeownership rate | 84.03 |
| Unemployment rate | 4.34 |
| Median home value | 322400 |
| Gini index | 0.3615 |
| Vacancy rate | 2.61 |
| White | 89865 |
| Black | 10573 |
| Asian | 4997 |
| Native | 929 |
| Hispanic/Latino | 30872 |
| Bachelor's or higher | 43982 |

## Districts

- [IL-14](/us/states/il/districts/14.md) — 100% (congressional)
- [IL Senate District 38](/us/states/il/districts/senate/38.md) — 86% (state senate)
- [IL Senate District 42](/us/states/il/districts/senate/42.md) — 8% (state senate)
- [IL Senate District 49](/us/states/il/districts/senate/49.md) — 6% (state senate)
- [IL House District 75](/us/states/il/districts/house/75.md) — 86% (state house)
- [IL House District 97](/us/states/il/districts/house/97.md) — 6% (state house)
- [IL House District 83](/us/states/il/districts/house/83.md) — 5% (state house)
- [IL House District 84](/us/states/il/districts/house/84.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
